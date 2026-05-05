BRICK = {
    "brick_num": 38,
    "brick_title": "Renal Imaging",
    "games": [
        {
            "slug": "imaging_modality_overview",
            "title": "Renal Imaging Modalities",
            "subtitle": "Match each modality to its key features",
            "categories": ["Primary Use", "Key Strength", "Notable Limitation"],
            "data": {
                "Renal Ultrasound": {
                    "Primary Use": "First-line study for kidney size, structure, obstruction",
                    "Key Strength": "Noninvasive, no radiation, preferred in pregnant patients",
                    "Notable Limitation": "Limited soft-tissue detail compared with CT or MRI"
                },
                "Noncontrast CT": {
                    "Primary Use": "Test of choice for nephrolithiasis evaluation",
                    "Key Strength": "Detects even small stones and identifies exact location",
                    "Notable Limitation": "Involves ionizing radiation exposure to patient"
                },
                "Contrast-Enhanced CT": {
                    "Primary Use": "Evaluates renal masses, trauma, abscesses, obstruction",
                    "Key Strength": "Distinguishes solid tumors from cysts and characterizes malignancy",
                    "Notable Limitation": "Requires IV contrast and ionizing radiation"
                },
                "Nuclear Renal Scan": {
                    "Primary Use": "Measures comparative function between two kidneys",
                    "Key Strength": "Determines differential function otherwise difficult to assess",
                    "Notable Limitation": "Provides functional rather than detailed anatomic detail"
                },
                "Renal MRI": {
                    "Primary Use": "Characterizes indeterminate renal masses",
                    "Key Strength": "High-resolution soft-tissue contrast without ionizing radiation",
                    "Notable Limitation": "Used when CT is indeterminate or contraindicated"
                }
            }
        },
        {
            "slug": "ultrasound_findings",
            "title": "Renal Ultrasound Findings",
            "subtitle": "Match each US finding to what it suggests",
            "categories": ["US Appearance", "Suggested Condition", "Clinical Implication"],
            "data": {
                "Hydronephrosis": {
                    "US Appearance": "Dilation of the renal collecting system on ultrasound",
                    "Suggested Condition": "Postrenal cause of obstruction such as stones or stricture",
                    "Clinical Implication": "May rapidly improve kidney function once obstruction relieved"
                },
                "Echogenic Kidneys": {
                    "US Appearance": "Bright echogenic appearance of cortex on ultrasound",
                    "Suggested Condition": "Chronic kidney disease with cortical thinning and atrophy",
                    "Clinical Implication": "Distinction reflects long-standing parenchymal damage"
                },
                "Multiple Anechoic Cysts": {
                    "US Appearance": "Large round anechoic lesions in bilateral kidneys",
                    "Suggested Condition": "Autosomal dominant polycystic kidney disease (ADPKD)",
                    "Clinical Implication": "Differentiates simple cysts from masses or abscesses"
                },
                "Doppler Flow Study": {
                    "US Appearance": "Color or spectral signal showing renal blood flow",
                    "Suggested Condition": "Suspected renal vascular disorder",
                    "Clinical Implication": "Assesses perfusion when vascular disease suspected"
                },
                "Normal Kidney": {
                    "US Appearance": "Smooth contour with normal cortex and no dilation",
                    "Suggested Condition": "No obstruction, mass, or chronic parenchymal change",
                    "Clinical Implication": "Reassuring baseline against which abnormal scans compare"
                }
            }
        },
        {
            "slug": "clinical_scenario_choice",
            "title": "Choosing the Right Scan",
            "subtitle": "Pick the best modality for each clinical scenario",
            "categories": ["Best Imaging Modality", "Reason for Choice", "Example Finding"],
            "data": {
                "Suspected Kidney Stone": {
                    "Best Imaging Modality": "Noncontrast CT of the abdomen and pelvis",
                    "Reason for Choice": "Test of choice for nephrolithiasis with high sensitivity",
                    "Example Finding": "Small ureteral stone with upstream hydronephrosis seen"
                },
                "Pregnant Patient with Flank Pain": {
                    "Best Imaging Modality": "Renal sonography (ultrasound)",
                    "Reason for Choice": "Preferred over CT because no radiation exposure",
                    "Example Finding": "Hydronephrosis suggesting obstruction without fetal risk"
                },
                "Indeterminate Renal Mass": {
                    "Best Imaging Modality": "Renal MRI with high-resolution soft-tissue contrast",
                    "Reason for Choice": "Excellent when CT is indeterminate or contraindicated",
                    "Example Finding": "Benign angiomyolipoma revealed on T1 imaging"
                },
                "Pre-Nephrectomy Planning": {
                    "Best Imaging Modality": "Nuclear medicine renal scan with radioisotope",
                    "Reason for Choice": "Confirms remaining kidney is functional before removal",
                    "Example Finding": "One nonfunctional kidney with normal contralateral uptake"
                },
                "Suspected Renal Vascular Disease": {
                    "Best Imaging Modality": "Doppler renal ultrasound",
                    "Reason for Choice": "Assesses renal blood flow noninvasively at bedside",
                    "Example Finding": "Abnormal arterial waveforms suggesting stenosis"
                }
            }
        }
    ]
}
