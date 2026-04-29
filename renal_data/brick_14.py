BRICK = {
    "brick_num": 14,
    "brick_title": "Osmotic Diuretics",
    "games": [
        {
            "slug": "osmotic_agents_overview",
            "title": "Osmotic Agents: Identity & Action",
            "subtitle": "Match each agent with its mechanism and clinical use",
            "categories": ["Route", "Mechanism", "Primary Clinical Use"],
            "data": {
                "Mannitol": {
                    "Route": "Given intravenously, most commonly used osmotic agent",
                    "Mechanism": "Diffuses poorly across cell membranes, freely filtered",
                    "Primary Clinical Use": "Reduce elevated intracranial pressure from brain injury"
                },
                "Pharmacologic Urea": {
                    "Route": "Given orally, less commonly used osmotic agent",
                    "Mechanism": "Filtered into nephron, increases free water excretion",
                    "Primary Clinical Use": "Treat chronic euvolemic hyponatremia such as SIADH"
                },
                "Hypertonic Saline": {
                    "Route": "Used more often than mannitol at some institutions",
                    "Mechanism": "Induces water movement out of cells like other osmotic agents",
                    "Primary Clinical Use": "Management of elevated intracranial pressure"
                }
            }
        },
        {
            "slug": "mannitol_mechanism_sites",
            "title": "Mannitol: Mechanism by Site",
            "subtitle": "How osmotic diuresis acts in body and nephron",
            "categories": ["Site of Action", "Effect on Water", "Net Result"],
            "data": {
                "Cells (extravascular)": {
                    "Site of Action": "Intracellular and extracellular fluid compartments",
                    "Effect on Water": "Draws water out of cells into the bloodstream",
                    "Net Result": "Reduces intracellular volume, decreases brain edema"
                },
                "Bloodstream": {
                    "Site of Action": "Plasma after IV mannitol administration",
                    "Effect on Water": "Increases serum osmolality, holds water intravascularly",
                    "Net Result": "Pulls water from tissues into circulation"
                },
                "Glomerulus": {
                    "Site of Action": "Renal filtration barrier",
                    "Effect on Water": "Mannitol freely filtered into tubular fluid",
                    "Net Result": "Delivers osmotic agent into nephron lumen"
                },
                "Proximal Tubule": {
                    "Site of Action": "Most marked effect, also descending loop of Henle",
                    "Effect on Water": "Increases tubular osmolarity, prevents water reabsorption",
                    "Net Result": "Sodium and water diuresis, increased urine output"
                }
            }
        },
        {
            "slug": "adverse_effects_contraindications",
            "title": "Adverse Effects & Contraindications",
            "subtitle": "Match each scenario with its mechanism and clinical concern",
            "categories": ["Type", "Underlying Mechanism", "Clinical Concern"],
            "data": {
                "Volume Depletion": {
                    "Type": "Adverse effect from excessive diuresis",
                    "Underlying Mechanism": "Severe water loss exceeds electrolyte loss",
                    "Clinical Concern": "Dehydration, hypernatremia, signs of poor perfusion"
                },
                "Volume Overload": {
                    "Type": "Adverse effect in poor kidney function",
                    "Underlying Mechanism": "Mannitol cannot be excreted, expands extracellular volume",
                    "Clinical Concern": "Plasma volume expansion worsens edema and CHF"
                },
                "Acute Kidney Injury": {
                    "Type": "Adverse effect on renal function",
                    "Underlying Mechanism": "Volume depletion, vasoconstriction, decreased GFR, raised creatinine",
                    "Clinical Concern": "Worsens kidney function, contributes to peripheral edema"
                },
                "Congestive Heart Failure": {
                    "Type": "Contraindication to osmotic diuretic use",
                    "Underlying Mechanism": "Increased plasma volume strains failing heart",
                    "Clinical Concern": "Risk of decompensation and pulmonary edema"
                },
                "Severe Renal Impairment": {
                    "Type": "Contraindication including anuria or chronic kidney disease",
                    "Underlying Mechanism": "Insufficient filtration leads to mannitol retention",
                    "Clinical Concern": "Risk of volume overload from retained drug"
                },
                "Severe Dehydration": {
                    "Type": "Contraindication in hypovolemic patients",
                    "Underlying Mechanism": "Already depleted patients lose more fluid with diuresis",
                    "Clinical Concern": "Hypotension and shock from excessive diuresis"
                }
            }
        }
    ]
}
