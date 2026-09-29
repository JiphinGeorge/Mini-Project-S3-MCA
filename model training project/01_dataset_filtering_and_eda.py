import os
import pandas as pd
import numpy as np

def run_filtering():
    print("=" * 80)
    print("STEP 1: MTSAMPLES DATASET FILTERING (8 MUTUALLY EXCLUSIVE SPECIALTIES)")
    print("=" * 80)
    
    # Paths
    raw_path = os.path.join("..", "Dataset", "mtsamples.csv")
    if not os.path.exists(raw_path):
        raw_path = os.path.join("Dataset", "mtsamples.csv")
        
    output_csv = "filtered_mtsamples_8classes.csv"
    
    print(f"Loading raw dataset from: {raw_path}")
    df = pd.read_csv(raw_path)
    print(f"Raw dataset shape: {df.shape}")
    
    # Drop rows missing transcription or medical specialty
    df = df.dropna(subset=['transcription', 'medical_specialty']).copy()
    
    # CRITICAL FIX: Strip leading/trailing whitespaces in medical_specialty
    df['medical_specialty'] = df['medical_specialty'].astype(str).str.strip()
    
    # Define the 8 Core Mutually Exclusive Clinical Specialties
    # (Removes administrative document formats like SOAP notes, Consults, Discharge Summaries,
    # and procedural umbrellas like general Surgery to avoid semantic ambiguity)
    target_specialties = [
        'Cardiovascular / Pulmonary',
        'Orthopedic',
        'Gastroenterology',
        'Neurology',
        'Urology',
        'Obstetrics / Gynecology',
        'ENT - Otolaryngology',
        'Ophthalmology'
    ]
    
    df_filtered = df[df['medical_specialty'].isin(target_specialties)].copy()
    
    # Prepare enriched clinical text: description (clinical summary) + transcription
    df_filtered['clinical_text'] = (
        df_filtered['description'].fillna('') + ' ' + df_filtered['transcription'].fillna('')
    ).str.strip()
    
    print("\n" + "=" * 60)
    print("DATASET FILTERING BREAKDOWN (8 CLINICAL SPECIALTIES):")
    print("=" * 60)
    print(f"Total Filtered Records : {len(df_filtered)}")
    print(f"Number of Specialties  : {len(target_specialties)}")
    print("-" * 60)
    
    counts = df_filtered['medical_specialty'].value_counts()
    for i, (spec, cnt) in enumerate(counts.items(), 1):
        pct = (cnt / len(df_filtered)) * 100
        print(f"{i:2d}. {spec:<28} : {cnt:>4d} samples ({pct:5.2f}%)")
    print("=" * 60)
    
    # Save clean dataset
    df_filtered.to_csv(output_csv, index=False)
    print(f"\nFiltered 8-specialty dataset successfully saved to: {os.path.abspath(output_csv)}")
    return output_csv

if __name__ == '__main__':
    run_filtering()
