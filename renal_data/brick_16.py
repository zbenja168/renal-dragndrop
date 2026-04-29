BRICK = {
    "brick_num": 16,
    "brick_title": "Body Fluids and Compartments",
    "games": [
        {
            "slug": "osmolality_vs_tonicity",
            "title": "Osmolality vs Tonicity",
            "subtitle": "Distinguish key features of osmolality and tonicity",
            "categories": ["Osmolality", "Tonicity", "Both"],
            "data": {
                "Definition": {
                    "Osmolality": "Total concentration of all osmotically active particles",
                    "Tonicity": "Concentration of solutes that cannot cross membranes",
                    "Both": "Measures of solute load affecting fluid balance"
                },
                "Calculation Formula": {
                    "Osmolality": "2x[Na+] + [Glucose]/18 + [BUN]/2.8",
                    "Tonicity": "2x[Na+] + [Glucose]/18 (no BUN)",
                    "Both": "Both rely on sodium as the major contributor"
                },
                "Includes Urea": {
                    "Osmolality": "Yes, urea contributes to total osmolality",
                    "Tonicity": "No, urea freely crosses cell membranes",
                    "Both": "Differ specifically based on urea inclusion"
                },
                "Effect on Cell Volume": {
                    "Osmolality": "Only changes cell volume if effective osmoles involved",
                    "Tonicity": "Always affects cell volume across membranes",
                    "Both": "Predict cellular response to fluid disturbances"
                },
                "Clinical Use": {
                    "Osmolality": "Used to calculate the osmolal gap",
                    "Tonicity": "Predicts water movement across cell membranes",
                    "Both": "Guide IV fluid therapy and electrolyte correction"
                }
            }
        },
        {
            "slug": "tonic_fluid_changes",
            "title": "Tonic Fluid Changes and Compartments",
            "subtitle": "Predict ICF/ECF shifts after isotonic, hypertonic, hypotonic changes",
            "categories": ["Effect on ECF", "Effect on ICF", "Clinical Example"],
            "data": {
                "Isotonic Gain": {
                    "Effect on ECF": "ECF expands; ~25% plasma, 75% interstitial",
                    "Effect on ICF": "No change; tonicity unchanged so no shift",
                    "Clinical Example": "Normal saline or balanced crystalloid infusion"
                },
                "Isotonic Loss": {
                    "Effect on ECF": "ECF volume decreases; tonicity unchanged",
                    "Effect on ICF": "ICF unchanged; no water shift occurs",
                    "Clinical Example": "Hemorrhage or severe diarrhea (isotonic dehydration)"
                },
                "Hypertonic Gain": {
                    "Effect on ECF": "ECF expands and becomes hypertonic",
                    "Effect on ICF": "ICF shrinks as water shifts into ECF",
                    "Clinical Example": "3% NaCl infusion or hyperglycemia"
                },
                "Hypertonic Loss": {
                    "Effect on ECF": "ECF becomes hypertonic from free water loss",
                    "Effect on ICF": "ICF shrinks; cellular dehydration occurs",
                    "Clinical Example": "Diabetes insipidus or inadequate water intake"
                },
                "Hypotonic Gain": {
                    "Effect on ECF": "ECF expands slightly and becomes hypotonic",
                    "Effect on ICF": "ICF expands as water shifts into cells",
                    "Clinical Example": "D5W or excess hypotonic fluid administration"
                },
                "Hypotonic Loss": {
                    "Effect on ECF": "ECF becomes hypotonic from excess water retention",
                    "Effect on ICF": "ICF expands; risk of cerebral edema",
                    "Clinical Example": "SIADH or excess hypotonic fluids"
                }
            }
        },
        {
            "slug": "iv_fluid_selection",
            "title": "IV Fluid Selection",
            "subtitle": "Match IV fluids to tonicity, effect, and clinical use",
            "categories": ["Tonicity", "Compartment Effect", "Key Indication or Risk"],
            "data": {
                "Normal Saline (0.9%)": {
                    "Tonicity": "Isotonic, ~308 mOsm/L with 154 mEq Na",
                    "Compartment Effect": "Expands ECF only; no ICF change",
                    "Key Indication or Risk": "Hypovolemia; risk of hyperchloremic acidosis"
                },
                "Lactated Ringer's": {
                    "Tonicity": "Isotonic balanced crystalloid with lactate buffer",
                    "Compartment Effect": "Expands ECF only without affecting ICF",
                    "Key Indication or Risk": "Volume resuscitation; balanced electrolyte composition"
                },
                "Plasma-Lyte": {
                    "Tonicity": "Isotonic, 294 mOsm/L; gluconate/acetate buffer",
                    "Compartment Effect": "Expands ECF; mimics plasma composition",
                    "Key Indication or Risk": "Balanced crystalloid for resuscitation"
                },
                "D5W": {
                    "Tonicity": "Hypotonic after dextrose metabolism (free water)",
                    "Compartment Effect": "Water shifts into ICF; expands both compartments",
                    "Key Indication or Risk": "Hypernatremia; risk of cerebral edema"
                },
                "Hypertonic Saline (3%)": {
                    "Tonicity": "Hypertonic, 1027 mOsm/L; 513 mEq Na",
                    "Compartment Effect": "Water shifts ICF to ECF; cells shrink",
                    "Key Indication or Risk": "Severe hyponatremia; risk of osmotic demyelination"
                },
                "Mannitol (20%)": {
                    "Tonicity": "Hypertonic, 1100 mOsm/L; no sodium added",
                    "Compartment Effect": "Pulls water from ICF to ECF; osmotic diuretic",
                    "Key Indication or Risk": "Elevated ICP or cerebral edema treatment"
                }
            }
        }
    ]
}
