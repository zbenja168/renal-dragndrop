BRICK = {
    "brick_num": 19,
    "brick_title": "Hypernatremia",
    "games": [
        {
            "slug": "hypernatremia_causes",
            "title": "Causes of Hypernatremia",
            "subtitle": "Match each cause to its mechanism and key feature",
            "categories": ["Category", "Mechanism", "Key Feature"],
            "data": {
                "Sweating": {
                    "Category": "Extrarenal water loss",
                    "Mechanism": "Loss of hypotonic fluid via skin",
                    "Key Feature": "Sweat sodium only 40 to 60 mEq/L"
                },
                "Diarrhea": {
                    "Category": "Extrarenal water loss",
                    "Mechanism": "Hypotonic GI fluid loss causing free water loss",
                    "Key Feature": "Common GI cause of hypernatremia"
                },
                "Diabetes Insipidus": {
                    "Category": "Renal water loss",
                    "Mechanism": "Lack of ADH or renal nonresponsiveness to ADH",
                    "Key Feature": "Aquaporins not inserted in collecting duct"
                },
                "Osmotic Diuresis": {
                    "Category": "Renal water loss",
                    "Mechanism": "Unexpected osmole drags water into urine",
                    "Key Feature": "Caused by glucose or mannitol"
                },
                "Sodium Bicarbonate Ampules": {
                    "Category": "Increased sodium intake",
                    "Mechanism": "Excess sodium load exceeds water intake",
                    "Key Feature": "Common in ICU during cardiac arrest"
                }
            }
        },
        {
            "slug": "central_vs_nephrogenic_di",
            "title": "Central vs Nephrogenic DI",
            "subtitle": "Compare the two main types of diabetes insipidus",
            "categories": ["Underlying Defect", "Common Cause", "Response to DDAVP"],
            "data": {
                "Central DI": {
                    "Underlying Defect": "Posterior pituitary fails to release sufficient ADH",
                    "Common Cause": "Idiopathic autoimmune attack on the pituitary",
                    "Response to DDAVP": "Urine osmolality rises and urine volume falls"
                },
                "Nephrogenic DI": {
                    "Underlying Defect": "Kidneys do not respond to circulating ADH",
                    "Common Cause": "Lithium therapy for bipolar disorder",
                    "Response to DDAVP": "No change in urine osmolality or volume"
                },
                "Pituitary Tumor DI": {
                    "Underlying Defect": "Tumor disrupts pituitary ADH release",
                    "Common Cause": "Pituitary or CNS tumor accounts for 40 percent",
                    "Response to DDAVP": "Urine concentrates after exogenous ADH given"
                },
                "Hypercalcemia DI": {
                    "Underlying Defect": "Calcium impairs collecting duct response to ADH",
                    "Common Cause": "Chronic hypercalcemia inhibits fluid concentration",
                    "Response to DDAVP": "Urine fails to concentrate after DDAVP"
                },
                "V2 Receptor Mutation DI": {
                    "Underlying Defect": "Defective V2 receptor on collecting duct cells",
                    "Common Cause": "Rare congenital mutation affecting ADH signaling",
                    "Response to DDAVP": "No change because receptor cannot respond"
                }
            }
        },
        {
            "slug": "hypernatremia_diagnosis_treatment",
            "title": "Diagnosis and Management",
            "subtitle": "Match clinical scenarios to lab findings and treatment",
            "categories": ["Severity or Test", "Clinical or Lab Finding", "Treatment Step"],
            "data": {
                "Mild Hypernatremia": {
                    "Severity or Test": "Sodium just above 145 mEq/L",
                    "Clinical or Lab Finding": "Thirst, fatigue, dry mucous membranes, poor turgor",
                    "Treatment Step": "Encourage oral water intake if able to drink"
                },
                "Severe Hypernatremia": {
                    "Severity or Test": "Sodium above 160 mEq/L",
                    "Clinical or Lab Finding": "Confusion, delirium, seizures, and coma",
                    "Treatment Step": "Lower sodium slowly at 10 mEq/L per 24 hours"
                },
                "Hypovolemic Patient": {
                    "Severity or Test": "Orthostatic hypotension and reduced skin turgor",
                    "Clinical or Lab Finding": "Decreased extracellular volume from sodium and water losses",
                    "Treatment Step": "Give isotonic IV fluids like 0.9 percent saline first"
                },
                "Extrarenal Water Loss": {
                    "Severity or Test": "Urine osmolality above 600 mOsm/kg",
                    "Clinical or Lab Finding": "Concentrated urine showing intact ADH response",
                    "Treatment Step": "Replace free water with D5W or half normal saline"
                },
                "Central DI Diagnosis": {
                    "Severity or Test": "Water deprivation followed by DDAVP",
                    "Clinical or Lab Finding": "Urine osmolality rises significantly after DDAVP",
                    "Treatment Step": "Give desmopressin to replace missing ADH"
                },
                "Nephrogenic DI Diagnosis": {
                    "Severity or Test": "Water deprivation followed by DDAVP",
                    "Clinical or Lab Finding": "No change in urine osmolality after DDAVP",
                    "Treatment Step": "Stop lithium and use thiazide or amiloride"
                }
            }
        }
    ]
}
