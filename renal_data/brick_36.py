BRICK = {
    "brick_num": 36,
    "brick_title": "End-Stage Kidney Disease and Replacement Therapy",
    "games": [
        {
            "slug": "krt_modalities",
            "title": "Kidney Replacement Therapy Modalities",
            "subtitle": "Compare transplant, hemodialysis, and peritoneal dialysis",
            "categories": ["Mechanism", "Setting/Access", "Key Feature"],
            "data": {
                "Renal Transplantation": {
                    "Mechanism": "Donor kidney placed in recipient pelvis, anastomosed to iliac vessels",
                    "Setting/Access": "Performed at large tertiary medical centers",
                    "Key Feature": "Preferred KRT with best mortality and quality of life benefits"
                },
                "In-center Hemodialysis": {
                    "Mechanism": "Blood filtered across semipermeable membrane via diffusion",
                    "Setting/Access": "Dialysis unit using AV fistula, graft, or catheter",
                    "Key Feature": "Typically intermittent treatments three times weekly"
                },
                "Peritoneal Dialysis": {
                    "Mechanism": "Dialysate in peritoneal cavity uses peritoneal capillaries for diffusion",
                    "Setting/Access": "Always done at home via surgically placed catheter",
                    "Key Feature": "Often automated by overnight cycler while patient sleeps"
                },
                "CRRT": {
                    "Mechanism": "Slow continuous hemodialysis over 24 hours",
                    "Setting/Access": "ICU setting via central venous access",
                    "Key Feature": "For AKI patients in shock who cannot tolerate rapid fluid shifts"
                }
            }
        },
        {
            "slug": "hemodialysis_vascular_access",
            "title": "Hemodialysis Vascular Access",
            "subtitle": "Compare access types for hemodialysis",
            "categories": ["Description", "Infection Risk", "Use Case"],
            "data": {
                "Arteriovenous Fistula": {
                    "Description": "Surgically created connection using patient's own vasculature",
                    "Infection Risk": "Extremely low risk of infection",
                    "Use Case": "Preferred long-term access, typically in nondominant arm"
                },
                "Synthetic AV Graft": {
                    "Description": "Synthetic tunneled conduit connecting artery and vein",
                    "Infection Risk": "Comparatively lower risk of infection",
                    "Use Case": "Alternative when patient's vasculature unsuitable for fistula"
                },
                "Tunneled Catheter": {
                    "Description": "Tunneled central venous catheter in IJ or subclavian",
                    "Infection Risk": "Large risk of infection",
                    "Use Case": "Used when fistula or graft not yet available"
                },
                "Non-tunneled Catheter": {
                    "Description": "Percutaneously placed central venous catheter",
                    "Infection Risk": "Large risk of infection",
                    "Use Case": "Short-term emergent or acute hemodialysis access"
                }
            }
        },
        {
            "slug": "dialysis_complications",
            "title": "Complications of Dialysis",
            "subtitle": "Recognize key complications and their causes",
            "categories": ["Description", "Cause/Mechanism", "Management"],
            "data": {
                "Vascular Access Thrombosis": {
                    "Description": "Common complication of AV fistulas and grafts",
                    "Cause/Mechanism": "Stenosis, fistula occlusion, or clot formation",
                    "Management": "Catheterization, balloon dilatation, surgical revision, plasminogen activator"
                },
                "Vascular Access Infection": {
                    "Description": "Most frequent in catheters, less in fistulas/grafts",
                    "Cause/Mechanism": "Even strict precautions cannot fully prevent line contamination",
                    "Management": "Antibiotics, sometimes catheter removal and exchange"
                },
                "Hypotension": {
                    "Description": "High-output heart failure or postural drops during dialysis",
                    "Cause/Mechanism": "Removal of 3-5 L over a treatment causes volume shifts",
                    "Management": "Adjust dry weight, slow ultrafiltration, manage orthostasis"
                },
                "Dialysis Amyloidosis": {
                    "Description": "Uncommon long-term complication after years of hemodialysis",
                    "Cause/Mechanism": "Beta-2-microglobulin not cleared by dialysis filter",
                    "Management": "Symptom control; resolves only after kidney transplant"
                },
                "Bacterial Peritonitis": {
                    "Description": "Most serious complication of peritoneal dialysis",
                    "Cause/Mechanism": "Skin flora like S. aureus or gram-negatives enter catheter",
                    "Management": "Intraperitoneal antibiotics; refractory cases need catheter removal"
                }
            }
        },
        {
            "slug": "dialysis_indications",
            "title": "Indications for Urgent Dialysis",
            "subtitle": "Recognize AEIOU criteria and chronic indications",
            "categories": ["Indication Type", "Specific Trigger", "Clinical Example"],
            "data": {
                "Acidosis": {
                    "Indication Type": "Acute urgent indication (AEIOU)",
                    "Specific Trigger": "Metabolic acidosis with pH below 7.1",
                    "Clinical Example": "Severe acidemia not reversible with medical management"
                },
                "Electrolytes": {
                    "Indication Type": "Acute urgent indication (AEIOU)",
                    "Specific Trigger": "Refractory hyperkalemia greater than 6.5 mEq/L",
                    "Clinical Example": "Potassium not controlled by medical therapy"
                },
                "Intoxications": {
                    "Indication Type": "Acute urgent indication (AEIOU)",
                    "Specific Trigger": "Dialyzable toxin overdose",
                    "Clinical Example": "Lithium, aspirin, ethylene glycol, or methanol toxicity"
                },
                "Overload": {
                    "Indication Type": "Acute urgent indication (AEIOU)",
                    "Specific Trigger": "Fluid overload refractory to diuresis",
                    "Clinical Example": "Volume overload not controlled by diuretics"
                },
                "Uremia": {
                    "Indication Type": "Acute or chronic indication",
                    "Specific Trigger": "Uremic signs and symptoms",
                    "Clinical Example": "Pericarditis, encephalopathy, pleuritis, or unexplained mental decline"
                }
            }
        }
    ]
}
