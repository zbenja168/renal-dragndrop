BRICK = {
    "brick_num": 6,
    "brick_title": "Glomerular Filtration Rate (GFR)",
    "games": [
        {
            "slug": "gfr_determinants",
            "title": "GFR Determinants & Filtration Fraction",
            "subtitle": "Match each parameter change with its hemodynamic effects",
            "categories": ["Effect on RBF", "Effect on GFR", "Effect on Filtration Fraction"],
            "data": {
                "Afferent arteriolar constriction": {
                    "Effect on RBF": "Decreases renal blood flow due to upstream resistance",
                    "Effect on GFR": "Decreases GFR from reduced glomerular hydrostatic pressure",
                    "Effect on Filtration Fraction": "Variable change; both RBF and GFR fall together"
                },
                "Efferent arteriolar constriction": {
                    "Effect on RBF": "Decreases renal blood flow from outflow obstruction",
                    "Effect on GFR": "Increases GFR via raised glomerular hydrostatic pressure",
                    "Effect on Filtration Fraction": "Increases; greater fraction of plasma becomes filtrate"
                },
                "Decreased plasma proteins": {
                    "Effect on RBF": "No change in renal blood flow occurs",
                    "Effect on GFR": "Increases GFR by lowering opposing oncotic pressure",
                    "Effect on Filtration Fraction": "Decreases as GFR rises without RBF change"
                },
                "Increased plasma proteins": {
                    "Effect on RBF": "No change in renal blood flow occurs",
                    "Effect on GFR": "Decreases GFR from elevated oncotic opposition",
                    "Effect on Filtration Fraction": "Increases relative to unchanged renal blood flow"
                },
                "Increased Kf": {
                    "Effect on RBF": "No change in renal blood flow occurs",
                    "Effect on GFR": "Increases GFR via greater membrane permeability",
                    "Effect on Filtration Fraction": "Increases as filtered fraction grows"
                },
                "Decreased Kf": {
                    "Effect on RBF": "No change in renal blood flow occurs",
                    "Effect on GFR": "Decreases GFR from scarring or mesangial contraction",
                    "Effect on Filtration Fraction": "Decreases due to reduced filtration capacity"
                }
            }
        },
        {
            "slug": "filtration_markers",
            "title": "Filtration Markers Comparison",
            "subtitle": "Match each marker with its properties and clinical use",
            "categories": ["Type/Source", "Key Limitation or Strength", "Clinical Use"],
            "data": {
                "Inulin": {
                    "Type/Source": "Exogenous fructose polysaccharide, gold standard marker",
                    "Key Limitation or Strength": "Freely filtered, not reabsorbed, secreted, or metabolized",
                    "Clinical Use": "Research reference standard; impractical for routine use"
                },
                "Creatinine": {
                    "Type/Source": "Endogenous waste from muscle creatine breakdown",
                    "Key Limitation or Strength": "Tubular secretion causes mild GFR overestimation",
                    "Clinical Use": "Standard surrogate via CKD-EPI or Cockcroft-Gault formulas"
                },
                "Cystatin C": {
                    "Type/Source": "Endogenous protein produced by all nucleated cells",
                    "Key Limitation or Strength": "Less affected by age, sex, and muscle mass",
                    "Clinical Use": "Alternative marker when creatinine is unreliable"
                },
                "Iothalamate": {
                    "Type/Source": "Exogenous iodinated radiocontrast agent",
                    "Key Limitation or Strength": "Requires specialized assay for measurement",
                    "Clinical Use": "Used in research and select clinical scenarios"
                }
            }
        },
        {
            "slug": "ckd_staging_consequences",
            "title": "KDIGO GFR Staging & Consequences",
            "subtitle": "Match each GFR range with its clinical implications",
            "categories": ["Functional Status", "Serum Creatinine Behavior", "Homeostatic Consequence"],
            "data": {
                "GFR over 60": {
                    "Functional Status": "Normal or near-normal kidney function",
                    "Serum Creatinine Behavior": "Small GFR changes produce minimal creatinine changes",
                    "Homeostatic Consequence": "Few disturbances; CKD requires additional damage evidence"
                },
                "GFR 15-60": {
                    "Functional Status": "Chronic kidney disease, progressively impaired function",
                    "Serum Creatinine Behavior": "Creatinine doubles for each halving of GFR",
                    "Homeostatic Consequence": "Predictable disturbances emerge across multiple organ systems"
                },
                "GFR under 15": {
                    "Functional Status": "End-stage renal disease requiring renal replacement",
                    "Serum Creatinine Behavior": "Substantially elevated creatinine with non-renal elimination",
                    "Homeostatic Consequence": "Cannot maintain homeostasis without dialysis or transplant"
                },
                "GFR under 30 (potassium)": {
                    "Functional Status": "Advanced CKD with reduced potassium handling",
                    "Serum Creatinine Behavior": "Markedly elevated; capacity declines nonlinearly",
                    "Homeostatic Consequence": "Hyperkalemia risk rises; avoid ACEi, ARBs, NSAIDs"
                },
                "GFR under 30 (acid-base)": {
                    "Functional Status": "Advanced CKD impairing ammonia and acid excretion",
                    "Serum Creatinine Behavior": "Elevated creatinine reflecting major nephron loss",
                    "Homeostatic Consequence": "Metabolic acidosis, edema, hypertension, fluid overload"
                }
            }
        }
    ]
}
