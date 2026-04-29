BRICK = {
    "brick_num": 20,
    "brick_title": "Antidiuretic Hormone Agonists",
    "games": [
        {
            "slug": "adh_agents_overview",
            "title": "ADH Agonists: Agent Profiles",
            "subtitle": "Match each agent to its properties",
            "categories": ["Vascular Effect", "Routes / Use", "Primary Indications"],
            "data": {
                "Desmopressin": {
                    "Vascular Effect": "Minimal vascular effect; selective V2 stimulation",
                    "Routes / Use": "Given nasally, orally, or intravenously",
                    "Primary Indications": "Central DI, bedwetting, von Willebrand disease"
                },
                "Vasopressin": {
                    "Vascular Effect": "Strong vasoconstrictor via V1 receptors",
                    "Routes / Use": "Given IV; not used for diabetes insipidus",
                    "Primary Indications": "Distributive shock and bleeding esophageal varices"
                },
                "Native ADH": {
                    "Vascular Effect": "Causes water reabsorption and arterial vasoconstriction",
                    "Routes / Use": "Secreted by posterior pituitary gland endogenously",
                    "Primary Indications": "Released for low blood pressure or high osmolarity"
                }
            }
        },
        {
            "slug": "vasopressin_receptors",
            "title": "Vasopressin Receptor Actions",
            "subtitle": "V1a versus V2 receptor effects",
            "categories": ["Location", "Mechanism", "Physiologic Effect"],
            "data": {
                "V2 Receptor": {
                    "Location": "Principal cells of the renal collecting duct",
                    "Mechanism": "Increases synthesis and insertion of aquaporin-2",
                    "Physiologic Effect": "Water reabsorption; concentrated urine produced"
                },
                "V1a Receptor (vascular)": {
                    "Location": "Vascular endothelial cells and arteriolar smooth muscle",
                    "Mechanism": "Smooth muscle contraction constricting arterioles",
                    "Physiologic Effect": "Raises blood pressure via vasoconstriction"
                },
                "V1a Receptor (platelet)": {
                    "Location": "Platelets in circulating blood",
                    "Mechanism": "Stimulates release of von Willebrand factor",
                    "Physiologic Effect": "Enhances platelet adhesion and clot formation"
                }
            }
        },
        {
            "slug": "adh_indications_adverse",
            "title": "Indications and Adverse Effects",
            "subtitle": "Clinical uses paired with potential harms",
            "categories": ["Underlying Problem", "Agent Used", "Adverse Effect Risk"],
            "data": {
                "Central Diabetes Insipidus": {
                    "Underlying Problem": "Insufficient ADH from hypothalamic neuron damage",
                    "Agent Used": "Desmopressin replaces deficient hormone for patients",
                    "Adverse Effect Risk": "IV desmopressin may cause hyponatremia from water reabsorption"
                },
                "Distributive Shock": {
                    "Underlying Problem": "Dilated arterioles from toxins or cytokines",
                    "Agent Used": "IV vasopressin reverses vasodilation and raises pressure",
                    "Adverse Effect Risk": "Pulmonary hypertension, mesenteric ischemia, skin necrosis"
                },
                "Bleeding Esophageal Varices": {
                    "Underlying Problem": "High portal vein pressures from chronic liver disease",
                    "Agent Used": "Injected vasopressin vasoconstricts veins to stop bleeding",
                    "Adverse Effect Risk": "Gut ischemia from strong V1-mediated vasoconstriction"
                },
                "Von Willebrand Disease": {
                    "Underlying Problem": "Deficient von Willebrand factor causing platelet defect",
                    "Agent Used": "Desmopressin enhances vWF release and platelet adhesion",
                    "Adverse Effect Risk": "Hyponatremia possible from renal water reabsorption"
                },
                "Nocturnal Enuresis": {
                    "Underlying Problem": "Bedwetting in children with normal ADH levels",
                    "Agent Used": "Desmopressin concentrates urine regardless of ADH level",
                    "Adverse Effect Risk": "Minimal vascular effects; watch for low sodium"
                }
            }
        }
    ]
}
