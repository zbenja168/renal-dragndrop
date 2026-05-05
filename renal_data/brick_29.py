BRICK = {
    "brick_num": 29,
    "brick_title": "Metabolic Alkalosis",
    "games": [
        {
            "slug": "alkalosis_pathophysiology_concepts",
            "title": "Pathophysiology Concepts",
            "subtitle": "Match phases and players in metabolic alkalosis",
            "categories": ["Definition", "Key Player", "Clinical Note"],
            "data": {
                "Generation Phase": {
                    "Definition": "Initial event causing net gain of bicarbonate in body",
                    "Key Player": "Alkali load such as vomiting, diuretics, or NaHCO3",
                    "Clinical Note": "Modest load raises HCO3 due to small extracellular pool"
                },
                "Maintenance Phase": {
                    "Definition": "Process keeping bicarbonate elevated despite renal filtration",
                    "Key Player": "Volume depletion and hypokalemia",
                    "Clinical Note": "Most crucial phase; explains persistent alkalosis"
                },
                "Pendrin Role": {
                    "Definition": "Cl/HCO3 exchanger in beta-intercalated cells",
                    "Key Player": "Chloride as exchange partner for bicarbonate secretion",
                    "Clinical Note": "Low Cl disables pendrin, kidney cannot secrete HCO3"
                },
                "Respiratory Compensation": {
                    "Definition": "Lung response to elevated blood pH",
                    "Key Player": "Brain respiratory center slowing ventilation",
                    "Clinical Note": "Hypoventilation raises PaCO2 but never fully corrects pH"
                }
            }
        },
        {
            "slug": "alkalosis_causes_classification",
            "title": "Causes of Metabolic Alkalosis",
            "subtitle": "Differentiate chloride-responsive vs chloride-resistant causes",
            "categories": ["Type", "Urine Chloride", "Volume Status"],
            "data": {
                "Vomiting": {
                    "Type": "Chloride-responsive metabolic alkalosis",
                    "Urine Chloride": "Less than 10 mEq/L",
                    "Volume Status": "Hypovolemia from gastric fluid loss"
                },
                "Prior Diuretic Use": {
                    "Type": "Chloride-responsive metabolic alkalosis",
                    "Urine Chloride": "Less than 10 mEq/L after diuretic stopped",
                    "Volume Status": "Hypovolemia from urinary salt and water loss"
                },
                "Bartter or Gitelman": {
                    "Type": "Chloride-resistant metabolic alkalosis",
                    "Urine Chloride": "Greater than 20 mEq/L",
                    "Volume Status": "Hypovolemia with normal blood pressure"
                },
                "Hyperaldosteronism": {
                    "Type": "Chloride-resistant metabolic alkalosis",
                    "Urine Chloride": "Greater than 20 mEq/L",
                    "Volume Status": "Hypertension with hypokalemia"
                },
                "Liddle Syndrome": {
                    "Type": "Chloride-resistant metabolic alkalosis",
                    "Urine Chloride": "Greater than 20 mEq/L",
                    "Volume Status": "Hypertension from ENaC overactivity"
                }
            }
        },
        {
            "slug": "alkalosis_diagnosis_management",
            "title": "Diagnosis and Management",
            "subtitle": "Match findings and treatments to alkalosis subtypes",
            "categories": ["Lab Findings", "Physical Exam", "Treatment"],
            "data": {
                "Chloride-Responsive": {
                    "Lab Findings": "High pH, high HCO3, high PaCO2, urine Cl under 10",
                    "Physical Exam": "Low BP, tachycardia, dry mucosa, decreased skin turgor",
                    "Treatment": "Normal saline to expand extracellular volume; replace potassium"
                },
                "Hyperaldosteronism": {
                    "Lab Findings": "High pH, hypokalemia, urine Cl over 20 mEq/L",
                    "Physical Exam": "Hypertension with normal volume status",
                    "Treatment": "Aldosterone antagonists plus potassium replacement"
                },
                "Liddle Syndrome": {
                    "Lab Findings": "High pH, low potassium, low aldosterone, low renin",
                    "Physical Exam": "Hypertension from constitutive ENaC activation",
                    "Treatment": "ENaC blockers like amiloride plus potassium"
                },
                "17-Hydroxylase Deficiency": {
                    "Lab Findings": "High pH, hypokalemia, abnormal adrenal steroid panel",
                    "Physical Exam": "Hypertension with congenital enzyme defect",
                    "Treatment": "Cortisol replacement plus potassium correction"
                },
                "Overall Workup": {
                    "Lab Findings": "Electrolytes, urine chloride, venous or arterial blood gas",
                    "Physical Exam": "Volume assessment plus blood pressure measurement",
                    "Treatment": "Address underlying cause; correct hypokalemia"
                }
            }
        }
    ]
}
