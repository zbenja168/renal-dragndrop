BRICK = {
    "brick_num": 34,
    "brick_title": "Acute Kidney Injury",
    "games": [
        {
            "slug": "aki_three_main_types",
            "title": "Three Main Types of AKI",
            "subtitle": "Match each AKI type to mechanism, common cause, and example",
            "categories": ["Mechanism", "Common Cause", "Example"],
            "data": {
                "Prerenal AKI": {
                    "Mechanism": "Problem with perfusion before blood reaches kidney tissue",
                    "Common Cause": "Volume depletion from vomiting, diarrhea, diuretics, hemorrhage",
                    "Example": "Cardiorenal syndrome with reduced cardiac output"
                },
                "Intrarenal AKI": {
                    "Mechanism": "Damage within the kidney tissue itself",
                    "Common Cause": "Acute tubular necrosis from ischemia, sepsis, or nephrotoxins",
                    "Example": "Acute interstitial nephritis from drugs"
                },
                "Postrenal AKI": {
                    "Mechanism": "Obstruction to urine flow after it leaves kidney",
                    "Common Cause": "Benign prostatic hyperplasia blocking urine outflow",
                    "Example": "Bilateral ureteral obstruction from stones"
                },
                "RPGN (intrarenal)": {
                    "Mechanism": "Rapidly worsening GFR from glomerular disease",
                    "Common Cause": "Goodpasture syndrome, lupus nephritis, IgA vasculitis",
                    "Example": "Postinfectious or membranoproliferative glomerulonephritis"
                }
            }
        },
        {
            "slug": "aki_diagnostic_findings",
            "title": "Diagnosing AKI: Key Lab Findings",
            "subtitle": "Match AKI type to urinalysis, FENa/Urine Na, and radiology",
            "categories": ["Urinalysis", "Urine Sodium / FENa", "Radiology"],
            "data": {
                "Prerenal AKI": {
                    "Urinalysis": "Normal urinalysis with no significant findings",
                    "Urine Sodium / FENa": "Urine Na less than 20 mEq/L, FENa under 1%",
                    "Radiology": "Normal renal ultrasound"
                },
                "ATN (intrarenal)": {
                    "Urinalysis": "Tubular epithelial cells and muddy brown casts",
                    "Urine Sodium / FENa": "Urine Na greater than 40 mEq/L, FENa above 2%",
                    "Radiology": "Normal renal ultrasound"
                },
                "Acute Interstitial Nephritis": {
                    "Urinalysis": "WBCs, WBC casts, and eosinophils on urinalysis",
                    "Urine Sodium / FENa": "Variable urine sodium and FENa values",
                    "Radiology": "Normal renal ultrasound"
                },
                "RPGN": {
                    "Urinalysis": "Proteinuria, dysmorphic RBCs, and RBC casts",
                    "Urine Sodium / FENa": "Variable urine sodium and FENa values",
                    "Radiology": "Normal renal ultrasound"
                },
                "Postrenal (stones/BPH)": {
                    "Urinalysis": "Hematuria with possible crystals from stones",
                    "Urine Sodium / FENa": "Variable urine sodium and FENa values",
                    "Radiology": "Hydronephrosis on ultrasound imaging"
                }
            }
        },
        {
            "slug": "aki_management_by_type",
            "title": "Managing AKI by Type",
            "subtitle": "Match AKI type to treatment goal, key intervention, and drug to avoid",
            "categories": ["Treatment Goal", "Key Intervention", "Drug or Action to Avoid"],
            "data": {
                "Prerenal AKI": {
                    "Treatment Goal": "Restore renal perfusion and effective volume",
                    "Key Intervention": "Volume repletion with isotonic 0.9% normal saline",
                    "Drug or Action to Avoid": "Avoid NSAIDs and ACE inhibitors during injury"
                },
                "Prerenal from Heart Failure": {
                    "Treatment Goal": "Treat heart failure without worsening perfusion",
                    "Key Intervention": "Diuretics, inotropic agents, and vasodilators given",
                    "Drug or Action to Avoid": "Avoid ACE inhibitors in this acute setting"
                },
                "Intrarenal AKI (ATN)": {
                    "Treatment Goal": "Stop ongoing tubular injury and stabilize disease",
                    "Key Intervention": "Stop toxic medications and correct hypotension or infection",
                    "Drug or Action to Avoid": "Avoid aminoglycosides and other nephrotoxins"
                },
                "RPGN": {
                    "Treatment Goal": "Suppress immune-mediated glomerular damage",
                    "Key Intervention": "Immunosuppressive therapy tailored to specific diagnosis",
                    "Drug or Action to Avoid": "Avoid delays before starting immunosuppression"
                },
                "Postrenal AKI": {
                    "Treatment Goal": "Urgently relieve urinary tract obstruction",
                    "Key Intervention": "Bladder catheter or nephrostomy tube placement",
                    "Drug or Action to Avoid": "Avoid leaving obstruction unrelieved"
                }
            }
        },
        {
            "slug": "aki_dialysis_aeiou",
            "title": "AEIOU Indications for Dialysis",
            "subtitle": "Match each AEIOU letter to its meaning and threshold or sign",
            "categories": ["Letter Stands For", "Clinical Meaning", "Threshold or Sign"],
            "data": {
                "A": {
                    "Letter Stands For": "Acidosis (metabolic)",
                    "Clinical Meaning": "Severe metabolic acidosis from failed acid excretion",
                    "Threshold or Sign": "Blood pH less than 7.1"
                },
                "E": {
                    "Letter Stands For": "Electrolyte imbalances",
                    "Clinical Meaning": "Severe hyperkalemia not controlled by medications",
                    "Threshold or Sign": "Potassium greater than 6.5 mEq/L"
                },
                "I": {
                    "Letter Stands For": "Intoxications",
                    "Clinical Meaning": "Some alcohol or drug poisonings cleared by dialysis",
                    "Threshold or Sign": "Toxic ingestion refractory to standard therapy"
                },
                "O": {
                    "Letter Stands For": "Overload (fluid)",
                    "Clinical Meaning": "Volume overload causing pulmonary edema or hypoxia",
                    "Threshold or Sign": "Fluid overload refractory to diuresis"
                },
                "U": {
                    "Letter Stands For": "Uremia",
                    "Clinical Meaning": "Toxin buildup with neurologic or cardiac signs",
                    "Threshold or Sign": "Pericarditis, encephalopathy, or unexplained mental decline"
                }
            }
        }
    ]
}
