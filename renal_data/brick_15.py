BRICK = {
    "brick_num": 15,
    "brick_title": "Potassium-Sparing Diuretics",
    "games": [
        {
            "slug": "drug_class_comparison",
            "title": "Aldosterone Antagonists vs ENaC Blockers",
            "subtitle": "Compare the two main classes of potassium-sparing diuretics",
            "categories": ["Drug Examples", "Mechanism of Action", "Site of Action"],
            "data": {
                "Spironolactone": {
                    "Drug Examples": "Aldosterone receptor antagonist; similar to sex steroid hormones",
                    "Mechanism of Action": "Competitively inhibits intracellular mineralocorticoid receptor",
                    "Site of Action": "Principal cells of the collecting duct in distal nephron"
                },
                "Eplerenone": {
                    "Drug Examples": "Aldosterone antagonist with fewer antiandrogen effects",
                    "Mechanism of Action": "Blocks mineralocorticoid receptor; inhibits Na+/K+-ATPase",
                    "Site of Action": "Principal cells of the collecting duct in distal nephron"
                },
                "Amiloride": {
                    "Drug Examples": "ENaC blocker often combined with hydrochlorothiazide",
                    "Mechanism of Action": "Directly blocks apical epithelial sodium channel",
                    "Site of Action": "Luminal ENaC channel of collecting duct principal cells"
                },
                "Triamterene": {
                    "Drug Examples": "ENaC blocker often combined with hydrochlorothiazide",
                    "Mechanism of Action": "Blocks luminal ENaC channel; reduces sodium reabsorption",
                    "Site of Action": "Luminal ENaC channel of collecting duct principal cells"
                }
            }
        },
        {
            "slug": "clinical_indications",
            "title": "Clinical Indications",
            "subtitle": "Match each condition to drug, rationale, and mechanism",
            "categories": ["Preferred Drug", "Rationale for Use", "Underlying Mechanism"],
            "data": {
                "Heart Failure (HFrEF)": {
                    "Preferred Drug": "Spironolactone or eplerenone as adjunct agent",
                    "Rationale for Use": "Reduces fluid retention; improves morbidity in NYHA II-IV",
                    "Underlying Mechanism": "Blocks aldosterone-induced retention and adverse cardiac remodeling"
                },
                "Cirrhosis with Ascites": {
                    "Preferred Drug": "Spironolactone is first-line diuretic of choice",
                    "Rationale for Use": "Pulls fluid from peritoneum; less hypokalemia than others",
                    "Underlying Mechanism": "Blocks aldosterone activation from end-stage liver disease"
                },
                "Hyperaldosteronism": {
                    "Preferred Drug": "Aldosterone receptor antagonists like spironolactone",
                    "Rationale for Use": "Treats hypertension and hypokalemia from adrenal hyperplasia",
                    "Underlying Mechanism": "Blocks unregulated aldosterone-driven Na+ retention and K+ loss"
                },
                "Hyperandrogenic States": {
                    "Preferred Drug": "Spironolactone only (eplerenone lacks antiandrogen effect)",
                    "Rationale for Use": "Treats female acne, hirsutism, polycystic ovarian syndrome",
                    "Underlying Mechanism": "Antiandrogen effects from sex steroid structural similarity"
                }
            }
        },
        {
            "slug": "adverse_effects_interactions",
            "title": "Adverse Effects and Drug Interactions",
            "subtitle": "Identify side effects and contraindicated combinations",
            "categories": ["What It Is", "Cause or Mechanism", "Clinical Concern"],
            "data": {
                "Hyperkalemia": {
                    "What It Is": "Elevated serum potassium from renal retention",
                    "Cause or Mechanism": "Drugs prevent K+ secretion in collecting duct cells",
                    "Clinical Concern": "Avoid in CKD; monitor potassium levels regularly"
                },
                "Type IV RTA": {
                    "What It Is": "Hyperkalemic normal anion gap metabolic acidosis",
                    "Cause or Mechanism": "Hyperkalemia suppresses proximal tubule ammonia synthesis",
                    "Clinical Concern": "Most often seen with aldosterone antagonists"
                },
                "Antiandrogen Effects": {
                    "What It Is": "Gynecomastia, decreased libido, sexual dysfunction in men",
                    "Cause or Mechanism": "Spironolactone similar to sex steroids; antiandrogen activity",
                    "Clinical Concern": "Less severe with eplerenone; consider switching"
                },
                "ACE Inhibitors and ARBs": {
                    "What It Is": "RAAS-inhibiting drugs like lisinopril and losartan",
                    "Cause or Mechanism": "Lower aldosterone levels, impair RAAS function further",
                    "Clinical Concern": "Combination may cause or worsen dangerous hyperkalemia"
                },
                "Pregnancy": {
                    "What It Is": "Spironolactone use during gestation",
                    "Cause or Mechanism": "Drug crosses the placenta with possible harm to fetus",
                    "Clinical Concern": "Discontinue spironolactone during pregnancy as precaution"
                }
            }
        }
    ]
}
