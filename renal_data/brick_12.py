BRICK = {
    "brick_num": 12,
    "brick_title": "Loop Diuretics",
    "games": [
        {
            "slug": "loop_diuretic_drugs",
            "title": "Loop Diuretic Drugs",
            "subtitle": "Match each drug to its potency and bioavailability",
            "categories": ["Relative Potency", "Oral Bioavailability", "Key Feature"],
            "data": {
                "Bumetanide": {
                    "Relative Potency": "Most potent loop diuretic, relative potency 1",
                    "Oral Bioavailability": "80% oral bioavailability",
                    "Key Feature": "Higher bioavailability and longer half-life than furosemide"
                },
                "Torsemide": {
                    "Relative Potency": "Relative potency 20, more potent than furosemide",
                    "Oral Bioavailability": "80% oral bioavailability",
                    "Key Feature": "Longer half-life than furosemide"
                },
                "Furosemide": {
                    "Relative Potency": "Relative potency 40, least potent of sulfonamides",
                    "Oral Bioavailability": "60% oral bioavailability",
                    "Key Feature": "Most commonly used loop diuretic agent"
                },
                "Ethacrynic Acid": {
                    "Relative Potency": "Relative potency 50-55, weakest of the four",
                    "Oral Bioavailability": "100% oral bioavailability",
                    "Key Feature": "Used in patients with sulfa drug sensitivity"
                }
            }
        },
        {
            "slug": "loop_diuretic_indications",
            "title": "Clinical Indications",
            "subtitle": "Match each condition to how loop diuretics help",
            "categories": ["Indication Type", "Mechanism of Benefit", "Notes"],
            "data": {
                "Pulmonary Edema in CHF": {
                    "Indication Type": "First-line treatment for severe edema",
                    "Mechanism of Benefit": "Reduces fluid overload via potent diuresis",
                    "Notes": "Most common use; relieves volume overload symptoms"
                },
                "Cirrhosis with Edema": {
                    "Indication Type": "First-line management of severe edema",
                    "Mechanism of Benefit": "Removes excess extracellular fluid",
                    "Notes": "Caution: depletion risks hepatic encephalopathy"
                },
                "Acute or Chronic Kidney Disease": {
                    "Indication Type": "Improves urine output",
                    "Mechanism of Benefit": "Forces diuresis despite low GFR",
                    "Notes": "Avoid in anuric AKI or anuric CKD patients"
                },
                "SIADH Hyponatremia": {
                    "Indication Type": "Treats hyponatremia from SIADH",
                    "Mechanism of Benefit": "Disrupts kidney urine concentration ability",
                    "Notes": "Loop combined with normal saline can correct sodium"
                },
                "Hyperkalemia": {
                    "Indication Type": "Treats elevated potassium levels",
                    "Mechanism of Benefit": "Increases urinary excretion of potassium",
                    "Notes": "Loss of K+/H+ via Na+/K+/2Cl- blockade"
                },
                "Hypercalcemia": {
                    "Indication Type": "Treats elevated calcium levels",
                    "Mechanism of Benefit": "Disrupts lumen-positive gradient driving Ca reabsorption",
                    "Notes": "Increases urinary calcium excretion"
                }
            }
        },
        {
            "slug": "loop_adverse_effects",
            "title": "Adverse Effects and Mechanisms",
            "subtitle": "Match each adverse effect to cause and consequence",
            "categories": ["Underlying Cause", "Clinical Consequence", "Notes"],
            "data": {
                "Volume Depletion": {
                    "Underlying Cause": "Excessive Na+ and water excretion in urine",
                    "Clinical Consequence": "Hypotension, prerenal AKI, decreased preload",
                    "Notes": "Can cause syncope or hepatic encephalopathy in liver disease"
                },
                "Hypokalemia": {
                    "Underlying Cause": "Increased urinary K+ loss from tubules",
                    "Clinical Consequence": "Increases risk of cardiac arrhythmias",
                    "Notes": "Activates RAAS, worsens K+ loss in collecting duct"
                },
                "Metabolic Alkalosis": {
                    "Underlying Cause": "Increased urinary H+ loss raises bicarbonate",
                    "Clinical Consequence": "Contraction alkalosis from fluid loss",
                    "Notes": "Aldosterone secretion further drives bicarbonate rise"
                },
                "Hypocalcemia and Hypomagnesemia": {
                    "Underlying Cause": "Decreased Ca2+ and Mg2+ reabsorption in TAL",
                    "Clinical Consequence": "Usually mild electrolyte disturbance",
                    "Notes": "Loss of lumen-positive gradient in thick ascending limb"
                },
                "Ototoxicity": {
                    "Underlying Cause": "Most frequent with rapid IV administration",
                    "Clinical Consequence": "Tinnitus, hearing loss, vertigo, ear fullness",
                    "Notes": "Ethacrynic acid causes this most often; usually reversible"
                },
                "NSAID Drug Interaction": {
                    "Underlying Cause": "NSAIDs decrease loop diuretic efficacy",
                    "Clinical Consequence": "Reduced vasodilatory and diuretic effect",
                    "Notes": "Avoid combining aspirin or ibuprofen with loop diuretics"
                }
            }
        }
    ]
}
