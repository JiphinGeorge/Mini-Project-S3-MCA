/**
 * MEDSPECIALTY AI PLATFORM - CLIENT ENGINE
 * Handles PDF extraction, preprocessing visualization, TF-IDF feature inspection,
 * multi-model prediction, soft voting consensus, and open-set rejection.
 */

// Sample Medical Transcriptions for Interactive Demonstration
const SAMPLE_TRANSCRIPTIONS = {
  cardiovascular: `CLINICAL SUMMARY:
The patient is a 64-year-old male admitted with acute coronary syndrome and crescendo angina. 
Emergency coronary angiography performed via right femoral approach demonstrated a 90% proximal left anterior descending (LAD) stenosis with TIMI-2 flow. 
Successful percutaneous coronary intervention (PCI) with balloon angioplasty and deployment of a 3.0 x 18 mm drug-eluting stent. Post-dilation angiogram showed 0% residual stenosis and restoration of TIMI-3 flow. 
Echocardiogram revealed mild anteroseptal hypokinesis with preserved left ventricular ejection fraction of 52%. Patient placed on dual antiplatelet therapy (aspirin and clopidogrel) and high-intensity atorvastatin.`,

  orthopedic: `OPERATIVE REPORT:
PREOPERATIVE DIAGNOSIS: Displaced intra-articular fracture of the distal radius, right wrist.
POSTOPERATIVE DIAGNOSIS: Displaced intra-articular fracture of the distal radius, right wrist.
PROCEDURE PERFORMED: Open reduction and internal fixation (ORIF) of right distal radius fracture with volar locking plate and screws.
PROCEDURE: The right upper extremity was prepped and draped in sterile fashion. A standard modified Henry approach was utilized. The pronator quadratus was reflected, exposing the fracture site. Hematoma evacuated and periosteum cleared. Anatomical reduction obtained under fluoroscopic visualization. A 2.4 mm variable-angle volar locking plate was positioned and secured with locking cortical and subchondral peg screws. Fluoroscopic examination confirmed anatomic reduction, articular congruity, and no screw penetration.`,

  neurology: `NEUROLOGICAL CONSULTATION:
Patient is a 58-year-old female presenting with acute onset right-sided hemiparesis, expressive aphasia, and facial droop. Symptoms commenced 2 hours prior to arrival.
NIH Stroke Scale (NIHSS) score on admission was 14. 
Brain MRI revealed acute diffusion restriction in the left middle cerebral artery (MCA) M2 branch territory consistent with acute ischemic stroke. Carotid duplex ultrasonography demonstrated 75% stenosis of the left internal carotid artery. 
Patient received IV thrombolysis and was admitted to the Neuro-Intensive Care Unit for continuous hemodynamic monitoring, neurological checks, and neuroprotective protocol.`,

  gastroenterology: `PROCEDURE NOTE:
PROCEDURE: Diagnostic and therapeutic colonoscopy with snare polypectomies.
INDICATIONS: Iron deficiency anemia and positive fecal occult blood test.
FINDINGS: The colonoscope was advanced under direct visualization to the cecum, confirmed by appendiceal orifice and ileocecal valve. In the ascending colon, a 15 mm sessile polyp was identified. Saline-epinephrine submucosal injection performed to create a safety cushion, followed by complete hot snare electrocautery resection. A second 8 mm pedunculated polyp in the sigmoid colon was excised by cold snare. Cecal mucosa and remaining colonic mucosa otherwise normal. Retrieved polyps submitted for histological analysis.`,

  ophthalmology: `SURGICAL OPERATIVE REPORT:
PROCEDURE: Phacoemulsification with posterior chamber intraocular lens (IOL) implantation, right eye.
SURGICAL DETAILS: Topical tetracaine and retrobulbar anesthesia administered. Clear corneal incision created at the 10 o'clock position with a 2.4 mm keratome. Continuous curvilinear capsulorhexis measuring 5.2 mm achieved under Viscoat viscoelastic protection. Hydrodissection performed confirming free rotation of nucleus. Phacoemulsification of nucleus completed using divide-and-conquer technique. Cortical remnants thoroughly aspirated with bimanual I/A. Foldable acrylic intraocular lens placed in capsular bag and centered. Paracentesis hydrated, eye left normotensive.`,

  dermatology: `DERMATOLOGY OUTPATIENT CLINIC:
Patient presents with chronic pruritic erythematous plaques covered by thick, silvery-white micaceous scales localized over bilateral extensor surfaces of elbows, patellar regions, and presacral area. Pitted indentations observed on fingernails. 
Clinical appearance pathognomonic for plaque psoriasis vulgaris. 
Prescribed topical calcipotriene and betamethasone dipropionate ointment twice daily, supplemented with gentle emollient therapy. Instructed on avoiding known triggers. Recommended follow-up in 6 weeks for response evaluation.`,

  psychiatry: `PSYCHIATRIC EVALUATION:
A 35-year-old female presents with persistent depressed mood, profound anhedonia, severe early morning awakening insomnia, psychomotor retardation, and guilt for the past 4 months.
Mental Status Examination: Patient appears fatigued with poor eye contact. Speech is slow, monotonous. Affect is restricted, flat, and mood depressed. Thought process logical, but ruminative on feelings of worthlessness.
Diagnosis: Major Depressive Disorder, single episode, severe without psychotic features.
Plan: Initiate SSRI antidepressant Sertraline 50 mg daily, titrated to 100 mg after 2 weeks, combined with weekly cognitive behavioral therapy (CBT).`
};

// Global App State
let currentSelectedFile = null;
let currentAnalysisResult = null;

document.addEventListener("DOMContentLoaded", () => {
  initializeNavigation();
  initializeInputModes();
  initializePdfUpload();
  initializeTextEditor();
  initializeFeatureSearch();
  initializeWeightSimulator();
  loadSample('cardiovascular'); // Load default clinical sample
});

// -------------------------------------------------------------
// 1. Navigation Tab Handling
// -------------------------------------------------------------
function initializeNavigation() {
  const tabs = document.querySelectorAll(".nav-tab-btn");
  const views = document.querySelectorAll(".view-section");

  tabs.forEach(tab => {
    tab.addEventListener("click", () => {
      const targetView = tab.getAttribute("data-target");

      tabs.forEach(t => t.classList.remove("active"));
      views.forEach(v => v.classList.remove("active-view"));

      tab.classList.add("active");
      const targetEl = document.getElementById(targetView);
      if (targetEl) targetEl.classList.add("active-view");

      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });
}

function switchView(viewId) {
  const tabBtn = document.querySelector(`.nav-tab-btn[data-target="${viewId}"]`);
  if (tabBtn) tabBtn.click();
}

// -------------------------------------------------------------
// 2. Input Mode Toggle (PDF vs Manual)
// -------------------------------------------------------------
function initializeInputModes() {
  const pdfModeBtn = document.getElementById("modePdfBtn");
  const textModeBtn = document.getElementById("modeTextBtn");
  const pdfContainer = document.getElementById("pdfUploadSection");

  if (pdfModeBtn && textModeBtn && pdfContainer) {
    pdfModeBtn.addEventListener("click", () => {
      pdfModeBtn.classList.add("active");
      textModeBtn.classList.remove("active");
      pdfContainer.style.display = "block";
    });

    textModeBtn.addEventListener("click", () => {
      textModeBtn.classList.add("active");
      pdfModeBtn.classList.remove("active");
      pdfContainer.style.display = "none";
    });
  }
}

// -------------------------------------------------------------
// 3. PDF Upload & Text Extraction
// -------------------------------------------------------------
function initializePdfUpload() {
  const dropzone = document.getElementById("pdfDropzone");
  const fileInput = document.getElementById("pdfFileInput");
  const selectedFileCard = document.getElementById("selectedFileCard");
  const fileNameDisplay = document.getElementById("selectedFileName");
  const fileSizeDisplay = document.getElementById("selectedFileSize");
  const extractBtn = document.getElementById("extractPdfBtn");
  const removeBtn = document.getElementById("removeFileBtn");

  if (!dropzone || !fileInput) return;

  dropzone.addEventListener("click", () => fileInput.click());

  // Drag and Drop Events
  ["dragenter", "dragover"].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      dropzone.classList.add("dragover");
    });
  });

  ["dragleave", "drop"].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      dropzone.classList.remove("dragover");
    });
  });

  dropzone.addEventListener("drop", (e) => {
    const files = e.dataTransfer.files;
    if (files.length > 0) handleSelectedFile(files[0]);
  });

  fileInput.addEventListener("change", (e) => {
    if (e.target.files.length > 0) handleSelectedFile(e.target.files[0]);
  });

  removeBtn.addEventListener("click", () => {
    currentSelectedFile = null;
    fileInput.value = "";
    selectedFileCard.style.display = "none";
    dropzone.style.display = "block";
  });

  extractBtn.addEventListener("click", async () => {
    if (!currentSelectedFile) return;
    await performPdfExtraction(currentSelectedFile);
  });
}

function handleSelectedFile(file) {
  if (!file.name.toLowerCase().endsWith(".pdf")) {
    alert("Please select a valid medical PDF document.");
    return;
  }

  currentSelectedFile = file;
  const dropzone = document.getElementById("pdfDropzone");
  const selectedFileCard = document.getElementById("selectedFileCard");
  const fileNameDisplay = document.getElementById("selectedFileName");
  const fileSizeDisplay = document.getElementById("selectedFileSize");

  fileNameDisplay.textContent = file.name;
  fileSizeDisplay.textContent = `${(file.size / 1024).toFixed(1)} KB`;

  dropzone.style.display = "none";
  selectedFileCard.style.display = "flex";
}

async function performPdfExtraction(file) {
  const extractBtn = document.getElementById("extractPdfBtn");
  const originalHtml = extractBtn.innerHTML;
  extractBtn.disabled = true;
  extractBtn.innerHTML = `<span>Extracting text...</span>`;

  try {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("/api/extract-pdf", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    if (!data.success) {
      alert(data.error || "Failed to extract text from PDF.");
      return;
    }

    const textarea = document.getElementById("transcriptionText");
    textarea.value = data.extracted_text;
    updateCounters();

    // Show temporary extraction success badge
    extractBtn.innerHTML = `<span>✓ Extracted ${data.word_count} Words</span>`;
    setTimeout(() => {
      extractBtn.innerHTML = originalHtml;
      extractBtn.disabled = false;
    }, 2500);

  } catch (error) {
    alert("An error occurred during PDF text extraction: " + error.message);
    extractBtn.innerHTML = originalHtml;
    extractBtn.disabled = false;
  }
}

// -------------------------------------------------------------
// 4. Transcription Editor & Preprocessing
// -------------------------------------------------------------
function initializeTextEditor() {
  const textarea = document.getElementById("transcriptionText");
  const clearBtn = document.getElementById("clearTextBtn");
  const analyzeBtn = document.getElementById("analyzeBtn");

  if (textarea) {
    textarea.addEventListener("input", updateCounters);
  }

  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      textarea.value = "";
      updateCounters();
      resetPipeline();
    });
  }

  if (analyzeBtn) {
    analyzeBtn.addEventListener("click", runClinicalAnalysis);
  }
}

function updateCounters() {
  const text = document.getElementById("transcriptionText").value;
  const charCount = text.length;
  const wordCount = text.trim() ? text.trim().split(/\s+/).length : 0;

  document.getElementById("charCountDisplay").textContent = `${charCount} Characters`;
  document.getElementById("wordCountDisplay").textContent = `${wordCount} Words`;
}

function loadSample(specialtyKey) {
  const sample = SAMPLE_TRANSCRIPTIONS[specialtyKey];
  if (sample) {
    const textarea = document.getElementById("transcriptionText");
    textarea.value = sample.trim();
    updateCounters();
  }
}

function resetPipeline() {
  document.querySelectorAll(".pipe-step-card").forEach(c => {
    c.classList.remove("completed", "active");
  });
}

// -------------------------------------------------------------
// 5. Run Full End-to-End Clinical Analysis
// -------------------------------------------------------------
async function runClinicalAnalysis() {
  const textarea = document.getElementById("transcriptionText");
  const text = textarea.value.trim();

  if (!text) {
    alert("Please enter or extract clinical transcription text before analyzing.");
    return;
  }

  const analyzeBtn = document.getElementById("analyzeBtn");
  const originalBtnContent = analyzeBtn.innerHTML;
  analyzeBtn.disabled = true;
  analyzeBtn.innerHTML = `<span>Inferencing Ensemble...</span>`;

  // Step Animation
  animatePipelineSteps();

  try {
    // 1. Call Preprocessing API
    const prepPromise = fetch("/api/preprocess", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    }).then(r => r.json());

    // 2. Call Feature Extraction API
    const featPromise = fetch("/api/features", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    }).then(r => r.json());

    // 3. Call Model Prediction API
    const predPromise = fetch("/api/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, threshold: 0.48 })
    }).then(r => r.json());

    const [prepData, featData, predData] = await Promise.all([prepPromise, featPromise, predPromise]);

    currentAnalysisResult = { prepData, featData, predData };

    // Render Results
    renderPredictionResults(predData);
    renderFeaturesTable(featData);
    renderPreprocessingInspector(prepData);

    // Complete all pipeline step cards
    document.querySelectorAll(".pipe-step-card").forEach(c => {
      c.classList.remove("active");
      c.classList.add("completed");
    });

  } catch (error) {
    alert("Inference failed: " + error.message);
  } finally {
    analyzeBtn.disabled = false;
    analyzeBtn.innerHTML = originalBtnContent;
  }
}

function animatePipelineSteps() {
  const steps = document.querySelectorAll(".pipe-step-card");
  steps.forEach(s => s.classList.remove("completed", "active"));

  let currentIdx = 0;
  const interval = setInterval(() => {
    if (currentIdx < steps.length) {
      if (currentIdx > 0) {
        steps[currentIdx - 1].classList.remove("active");
        steps[currentIdx - 1].classList.add("completed");
      }
      steps[currentIdx].classList.add("active");
      currentIdx++;
    } else {
      clearInterval(interval);
    }
  }, 90);
}

// -------------------------------------------------------------
// 6. Render Prediction Decision Cards & Probability Distribution
// -------------------------------------------------------------
function renderPredictionResults(pred) {
  const card = document.getElementById("specialtyDecisionCard");
  const decisionTag = document.getElementById("decisionTagBadge");
  const specialtyTitle = document.getElementById("predictedSpecialtyTitle");
  const specialtySubtitle = document.getElementById("predictedSpecialtySubtitle");
  const meterValuePct = document.getElementById("meterValuePct");
  const meterBarFill = document.getElementById("meterBarFill");
  const latencyBadge = document.getElementById("inferenceLatencyDisplay");
  const outOfScopeNotice = document.getElementById("outOfScopeNotice");
  const candidateChipsRow = document.getElementById("candidateChipsRow");

  // Latency & Features Telemetry
  latencyBadge.textContent = `${pred.inference_time_ms} ms • ${pred.vocabulary_matches} Terms Matched`;

  const confPercent = pred.confidence_percent;
  meterValuePct.textContent = confPercent;
  meterBarFill.style.width = confPercent;

  if (pred.is_other) {
    // Open-Set Rejection Triggered (< 48%)
    card.className = "decision-card other-card";
    decisionTag.className = "decision-tag tag-other";
    decisionTag.innerHTML = `<span>● OUT OF SCOPE / REQUIRES REVIEW</span>`;

    specialtyTitle.textContent = "Other";
    specialtySubtitle.textContent = pred.explanation;

    meterBarFill.className = "meter-bar-fill fill-other";

    // Show Out-of-Scope Warning Notice
    outOfScopeNotice.style.display = "block";
    candidateChipsRow.innerHTML = "";
    if (pred.nearest_candidates && pred.nearest_candidates.length > 0) {
      pred.nearest_candidates.forEach(cand => {
        const chip = document.createElement("div");
        chip.className = "candidate-chip";
        chip.innerHTML = `<span>${cand.specialty}</span> <strong>${cand.percent}</strong>`;
        candidateChipsRow.appendChild(chip);
      });
    }

  } else {
    // Confirmed In-Domain Specialty (>= 48%)
    card.className = "decision-card confirmed-card";
    decisionTag.className = "decision-tag tag-confirmed";
    decisionTag.innerHTML = `<span>✓ IN-DOMAIN SPECIALTY CONFIRMED</span>`;

    specialtyTitle.textContent = pred.predicted_specialty;
    specialtySubtitle.textContent = pred.explanation;

    meterBarFill.className = "meter-bar-fill fill-confirmed";
    outOfScopeNotice.style.display = "none";
  }

  // Render 8-Class Probability Distribution Bars
  renderProbabilityBars(pred.probability_distribution);

  // Render 4-Model Breakdown
  renderModelsGrid(pred.models_breakdown);
}

function renderProbabilityBars(probDist) {
  const listContainer = document.getElementById("probDistList");
  listContainer.innerHTML = "";

  for (const [specialty, prob] of Object.entries(probDist)) {
    const pct = (prob * 100).toFixed(1);

    const row = document.createElement("div");
    row.className = "prob-row-item";
    row.innerHTML = `
      <div class="prob-item-header">
        <span>${specialty}</span>
        <span class="prob-item-val">${pct}%</span>
      </div>
      <div class="prob-item-bar">
        <div class="prob-item-fill" style="width: ${pct}%"></div>
      </div>
    `;
    listContainer.appendChild(row);
  }
}

function renderModelsGrid(models) {
  const gridContainer = document.getElementById("modelsGridContainer");
  if (!gridContainer || !models) return;

  gridContainer.innerHTML = "";

  const modelKeys = ["svm", "lr", "rf", "mnb"];
  modelKeys.forEach(k => {
    const m = models[k];
    if (!m) return;

    const miniCard = document.createElement("div");
    miniCard.className = "mini-model-card";
    miniCard.innerHTML = `
      <div class="mini-model-header">
        <span class="mini-model-name">${m.name}</span>
        <span class="mini-weight-tag">Weight: ${m.weight}</span>
      </div>
      <div class="mini-pred-specialty">${m.predicted_specialty}</div>
      <div class="mini-pred-pct">Posterior: <strong>${m.confidence_percent}</strong> • Acc: ${m.accuracy}%</div>
    `;
    gridContainer.appendChild(miniCard);
  });
}

// -------------------------------------------------------------
// 7. Render TF-IDF Features Table
// -------------------------------------------------------------
function renderFeaturesTable(featData) {
  const tbody = document.getElementById("featuresTableBody");
  const totalMatchesBadge = document.getElementById("activeFeaturesCountBadge");
  const sparsityBadge = document.getElementById("vectorSparsityBadge");

  if (totalMatchesBadge) totalMatchesBadge.textContent = featData.non_zero_count;
  if (sparsityBadge) sparsityBadge.textContent = `${featData.sparsity_pct}%`;

  if (!tbody) return;
  tbody.innerHTML = "";

  if (!featData.top_features || featData.top_features.length === 0) {
    tbody.innerHTML = `<tr><td colspan="5" style="text-align: center; color: var(--text-muted); padding: 24px;">No clinical features extracted yet. Run analysis first.</td></tr>`;
    return;
  }

  featData.top_features.forEach((f, idx) => {
    const tr = document.createElement("tr");
    const chipClass = f.type === "Bigram" ? "ngram-bigram" : "ngram-unigram";

    tr.innerHTML = `
      <td class="mono-cell">#${idx + 1}</td>
      <td><strong>${f.feature}</strong></td>
      <td><span class="ngram-chip ${chipClass}">${f.type}</span></td>
      <td class="mono-cell" style="color: var(--primary); font-weight: 700;">${f.score.toFixed(4)}</td>
      <td class="mono-cell">
        <div style="width: 100%; height: 6px; background-color: #E2E8F0; border-radius: 9999px; overflow: hidden;">
          <div style="width: ${Math.min(f.score * 200, 100)}%; height: 100%; background-color: var(--tertiary);"></div>
        </div>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function initializeFeatureSearch() {
  const searchInput = document.getElementById("featureSearchInput");
  if (!searchInput) return;

  searchInput.addEventListener("input", (e) => {
    const query = e.target.value.toLowerCase().trim();
    if (!currentAnalysisResult || !currentAnalysisResult.featData) return;

    const allFeatures = currentAnalysisResult.featData.all_features || [];
    const filtered = allFeatures.filter(f => f.feature.toLowerCase().includes(query));

    const tbody = document.getElementById("featuresTableBody");
    tbody.innerHTML = "";

    filtered.slice(0, 30).forEach((f, idx) => {
      const tr = document.createElement("tr");
      const chipClass = f.type === "Bigram" ? "ngram-bigram" : "ngram-unigram";

      tr.innerHTML = `
        <td class="mono-cell">#${idx + 1}</td>
        <td><strong>${f.feature}</strong></td>
        <td><span class="ngram-chip ${chipClass}">${f.type}</span></td>
        <td class="mono-cell" style="color: var(--primary); font-weight: 700;">${f.score.toFixed(4)}</td>
        <td class="mono-cell">
          <div style="width: 100%; height: 6px; background-color: #E2E8F0; border-radius: 9999px; overflow: hidden;">
            <div style="width: ${Math.min(f.score * 200, 100)}%; height: 100%; background-color: var(--tertiary);"></div>
          </div>
        </td>
      `;
      tbody.appendChild(tr);
    });
  });
}

function renderPreprocessingInspector(prepData) {
  // Can be viewed in modal or expandable inspector
  console.log("Preprocessing Stages:", prepData);
}

// -------------------------------------------------------------
// 8. Interactive Ensemble Weight Simulator (How It Works View)
// -------------------------------------------------------------
function initializeWeightSimulator() {
  const svmSlider = document.getElementById("svmWeightSlider");
  const lrSlider = document.getElementById("lrWeightSlider");
  const rfSlider = document.getElementById("rfWeightSlider");
  const mnbSlider = document.getElementById("mnbWeightSlider");

  if (!svmSlider) return;

  const updateWeights = () => {
    const wSvm = parseInt(svmSlider.value);
    const wLr = parseInt(lrSlider.value);
    const wRf = parseInt(rfSlider.value);
    const wMnb = parseInt(mnbSlider.value);

    document.getElementById("svmWeightVal").textContent = wSvm;
    document.getElementById("lrWeightVal").textContent = wLr;
    document.getElementById("rfWeightVal").textContent = wRf;
    document.getElementById("mnbWeightVal").textContent = wMnb;

    const totalWeight = wSvm + wLr + wRf + wMnb;
    document.getElementById("totalWeightSum").textContent = `Total Weight Divisor: ${totalWeight}`;
    document.getElementById("formulaWeights").textContent = `(${wSvm}×SVM + ${wLr}×LR + ${wRf}×RF + ${wMnb}×MNB) / ${totalWeight}`;
  };

  [svmSlider, lrSlider, rfSlider, mnbSlider].forEach(s => {
    s.addEventListener("input", updateWeights);
  });
}
