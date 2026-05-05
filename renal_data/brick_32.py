BRICK = {
    "brick_num": 32,
    "brick_title": "Carbonic Anhydrase Inhibitors",
    "games": [
        {
            "slug": "cai_drugs_administration",
            "title": "CAI Drugs and Routes",
            "subtitle": "Match each carbonic anhydrase inhibitor to its administration and indications",
            "categories": ["Administration", "Primary Indication", "Drug Class Suffix"],
            "data": {
                "Acetazolamide": {
                    "Administration": "Oral or IV systemic therapy",
                    "Primary Indication": "Altitude sickness, glaucoma, refractory seizures, hypertension",
                    "Drug Class Suffix": "Ends in -zolamide, contains sulfonamide group"
                },
                "Brinzolamide": {
                    "Administration": "Topical eye drop",
                    "Primary Indication": "Glaucoma (chronic long-term topical therapy)",
                    "Drug Class Suffix": "Ends in -zolamide, contains sulfonamide group"
                },
                "Dorzolamide": {
                    "Administration": "Topical eye drop",
                    "Primary Indication": "Glaucoma (chronic long-term topical therapy)",
                    "Drug Class Suffix": "Ends in -zolamide, contains sulfonamide group"
                },
                "Methazolamide": {
                    "Administration": "Oral systemic therapy",
                    "Primary Indication": "Glaucoma treatment",
                    "Drug Class Suffix": "Ends in -zolamide, contains sulfonamide group"
                }
            }
        },
        {
            "slug": "cai_organ_mechanisms",
            "title": "CAI Mechanisms by Organ",
            "subtitle": "Match each organ site to how CAIs act and what they treat there",
            "categories": ["CAI Effect at Site", "Clinical Use", "Key Physiology"],
            "data": {
                "Kidney (proximal tubule)": {
                    "CAI Effect at Site": "Block bicarbonate and sodium reabsorption, mild diuresis",
                    "Clinical Use": "Altitude sickness, COPD, central sleep apnea",
                    "Key Physiology": "CA needed for HCO3- reabsorption via Na+/H+ antiporter"
                },
                "Eye (ciliary body)": {
                    "CAI Effect at Site": "Decrease HCO3- and aqueous humor production",
                    "Clinical Use": "Open-angle glaucoma to lower intraocular pressure",
                    "Key Physiology": "Ciliary body uses CO2 and CA to make aqueous humor"
                },
                "Brain (choroid plexus)": {
                    "CAI Effect at Site": "Reduce bicarbonate and cerebrospinal fluid production",
                    "Clinical Use": "Idiopathic intracranial hypertension (pseudotumor cerebri)",
                    "Key Physiology": "Choroid plexus generates CSF circulating in subarachnoid space"
                },
                "CNS neurons": {
                    "CAI Effect at Site": "Reduce intracellular bicarbonate from high CA activity",
                    "Clinical Use": "Refractory seizures as secondary or tertiary therapy",
                    "Key Physiology": "High intracellular HCO3- drives uncoordinated neuronal firing"
                }
            }
        },
        {
            "slug": "cai_adverse_effects",
            "title": "CAI Adverse Effects and Cautions",
            "subtitle": "Match each adverse effect or contraindication to its mechanism and clinical clue",
            "categories": ["Mechanism", "Clinical Manifestation", "When It Appears"],
            "data": {
                "Metabolic acidosis": {
                    "Mechanism": "Renal bicarbonate wasting compensated by chloride retention",
                    "Clinical Manifestation": "Hyperchloremic non-anion gap acidosis with low serum HCO3-",
                    "When It Appears": "After several days of CAI therapy, self-limiting"
                },
                "Renal stones (nephrolithiasis)": {
                    "Mechanism": "Alkalinization of urine causes calcium phosphate precipitation",
                    "Clinical Manifestation": "Flank pain, hematuria from kidney stone formation",
                    "When It Appears": "With prolonged CAI use due to alkaline urine"
                },
                "Neurologic effects": {
                    "Mechanism": "Acid-base shifts and direct nerve effects from CA inhibition",
                    "Clinical Manifestation": "Paresthesias in extremities and tinnitus in ears",
                    "When It Appears": "Common during routine CAI dosing"
                },
                "Sulfa allergy reaction": {
                    "Mechanism": "CAIs contain a sulfonamide group cross-reacting with sulfa allergy",
                    "Clinical Manifestation": "Hypersensitivity reaction in sulfa-allergic patients",
                    "When It Appears": "Contraindication; avoid CAIs entirely in these patients"
                },
                "Hepatic encephalopathy": {
                    "Mechanism": "CAIs precipitate mental status changes in failing liver",
                    "Clinical Manifestation": "Confusion and altered mental status in cirrhotic patient",
                    "When It Appears": "When CAIs given to patients with cirrhosis"
                }
            }
        }
    ]
}
