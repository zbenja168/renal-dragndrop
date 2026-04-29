BRICK = {
    "brick_num": 18,
    "brick_title": "Hyponatremia",
    "games": [
        {
            "slug": "hyponatremia_types_by_tonicity",
            "title": "Types of Hyponatremia by Tonicity",
            "subtitle": "Match each type to its osmolality, mechanism, and example",
            "categories": ["Serum Osmolality", "Mechanism", "Example Cause"],
            "data": {
                "Hypotonic Hyponatremia": {
                    "Serum Osmolality": "Low (under 280 mOsm/kg H2O)",
                    "Mechanism": "True hyponatremia with osmotic shift into cells",
                    "Example Cause": "SIADH, heart failure, volume depletion"
                },
                "Isotonic (Pseudohyponatremia)": {
                    "Serum Osmolality": "Normal (280-295 mOsm/kg H2O)",
                    "Mechanism": "Lab artifact from non-aqueous portion of plasma",
                    "Example Cause": "Hyperlipidemia or multiple myeloma proteins"
                },
                "Hypertonic Hyponatremia": {
                    "Serum Osmolality": "High (over 295 mOsm/kg H2O)",
                    "Mechanism": "Osmotic pull of water out of cells dilutes sodium",
                    "Example Cause": "Hyperglycemia, often in uncontrolled diabetes"
                },
                "Hypotonic Hypovolemic": {
                    "Serum Osmolality": "Low with decreased extracellular volume",
                    "Mechanism": "Low ECV stimulates ADH release and water retention",
                    "Example Cause": "Vomiting, diarrhea, or diuretic overuse"
                },
                "Hypotonic Hypervolemic": {
                    "Serum Osmolality": "Low with increased extracellular volume",
                    "Mechanism": "Low effective volume activates RAAS and ADH",
                    "Example Cause": "Heart failure, cirrhosis, nephrotic syndrome"
                }
            }
        },
        {
            "slug": "siadh_causes",
            "title": "Causes of SIADH (Euvolemic Hyponatremia)",
            "subtitle": "Match each SIADH trigger to its category and example",
            "categories": ["Category", "Key Example", "Mechanism"],
            "data": {
                "Small Cell Lung Cancer": {
                    "Category": "Ectopic ADH-secreting tumor",
                    "Key Example": "Most important neoplastic cause of SIADH",
                    "Mechanism": "Tumor secretes ADH directly into circulation"
                },
                "Pulmonary Disease": {
                    "Category": "Lung cell ADH source",
                    "Key Example": "COPD, pneumonia, or tuberculosis",
                    "Mechanism": "Diseased lung cells produce ectopic ADH"
                },
                "Pain and Nausea": {
                    "Category": "Increased pituitary ADH",
                    "Key Example": "Nausea is a potent stimulus of ADH release",
                    "Mechanism": "Stimulates posterior pituitary ADH secretion"
                },
                "Drugs": {
                    "Category": "Medication-induced",
                    "Key Example": "SSRIs, carbamazepine, sulfonylureas, MDMA",
                    "Mechanism": "Drugs trigger or potentiate ADH release"
                },
                "CNS Disease": {
                    "Category": "Central nervous system disorder",
                    "Key Example": "Strokes, seizures, meningitis, schizophrenia",
                    "Mechanism": "CNS pathology drives inappropriate ADH release"
                },
                "Adrenal Insufficiency": {
                    "Category": "Endocrine cause",
                    "Key Example": "Low cortisol with elevated CRH",
                    "Mechanism": "Low cortisol stimulates pituitary ADH release"
                }
            }
        },
        {
            "slug": "hyponatremia_management",
            "title": "Management of Hyponatremia",
            "subtitle": "Match each scenario to first-line treatment and key risk",
            "categories": ["Volume Status", "First-Line Treatment", "Key Caution"],
            "data": {
                "Hypovolemic Hyponatremia": {
                    "Volume Status": "Decreased extracellular volume",
                    "First-Line Treatment": "Correct volume depletion with normal saline",
                    "Key Caution": "Avoid rapid correction to prevent demyelination"
                },
                "Hypervolemic Hyponatremia": {
                    "Volume Status": "Increased extracellular volume from CHF or cirrhosis",
                    "First-Line Treatment": "Loop diuretics to diurese to normal volume",
                    "Key Caution": "Liver disease may ultimately require transplant"
                },
                "Acute Symptomatic SIADH": {
                    "Volume Status": "Euvolemic with neurologic symptoms under 48 hours",
                    "First-Line Treatment": "3% hypertonic saline given cautiously",
                    "Key Caution": "Sodium rise no more than 4-6 mEq/L per 24 hours"
                },
                "Chronic SIADH": {
                    "Volume Status": "Euvolemic with longstanding hyponatremia",
                    "First-Line Treatment": "Water restriction, loop diuretics, ADH antagonists",
                    "Key Caution": "Increase solute intake using urea or salt tablets"
                },
                "Pseudohyponatremia": {
                    "Volume Status": "Isotonic lab artifact",
                    "First-Line Treatment": "No treatment needed for sodium itself",
                    "Key Caution": "Test for hyperlipidemia or multiple myeloma"
                },
                "Hypertonic Hyponatremia": {
                    "Volume Status": "Hyperosmolar from hyperglycemia",
                    "First-Line Treatment": "Lower blood glucose with insulin or other agents",
                    "Key Caution": "Sodium falls about 1.6 mEq/L per 100 glucose rise"
                }
            }
        }
    ]
}
