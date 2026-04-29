BRICK = {
    "brick_num": 5,
    "brick_title": "Glomerular Function",
    "games": [
        {
            "slug": "size_charge_selectivity",
            "title": "Size and Charge Selectivity",
            "subtitle": "Match solutes to filtration classification, weight, and radius",
            "categories": ["Classification", "Molecular Weight", "Molecular Radius"],
            "data": {
                "Water and Electrolytes": {
                    "Classification": "Freely filtered across barrier",
                    "Molecular Weight": "Less than 20 kDa",
                    "Molecular Radius": "Less than 2 nm"
                },
                "Beta-2 Microglobulin": {
                    "Classification": "Partially restricted small protein",
                    "Molecular Weight": "Approximately 20-70 kDa range",
                    "Molecular Radius": "Between 2 and 4 nm"
                },
                "Albumin": {
                    "Classification": "Largely excluded under normal conditions",
                    "Molecular Weight": "Approximately 66 kDa",
                    "Molecular Radius": "Approximately 3.6 nm, charge-restricted"
                },
                "IgG and Globulins": {
                    "Classification": "Excluded by size barrier",
                    "Molecular Weight": "Greater than 70 kDa",
                    "Molecular Radius": "Greater than 4 nm"
                },
                "Glucose and Urea": {
                    "Classification": "Freely filtered small solutes",
                    "Molecular Weight": "Well below 20 kDa",
                    "Molecular Radius": "Much less than 2 nm"
                }
            }
        },
        {
            "slug": "starling_forces_nfp",
            "title": "Starling Forces and Net Filtration Pressure",
            "subtitle": "Identify each force's value, role, and effect on filtration",
            "categories": ["Normal Value", "Effect on Filtration", "Primary Determinant"],
            "data": {
                "Glomerular Hydrostatic Pressure": {
                    "Normal Value": "Approximately 55 mmHg",
                    "Effect on Filtration": "Favors filtration out of capillary",
                    "Primary Determinant": "Renal blood flow and arteriolar resistance"
                },
                "Bowman Space Hydrostatic Pressure": {
                    "Normal Value": "Approximately 15 mmHg",
                    "Effect on Filtration": "Opposes filtration into Bowman space",
                    "Primary Determinant": "Tubular fluid flow and outflow obstruction"
                },
                "Glomerular Oncotic Pressure": {
                    "Normal Value": "Averages about 30 mmHg",
                    "Effect on Filtration": "Opposes filtration along capillary length",
                    "Primary Determinant": "Plasma protein concentration, mainly albumin"
                },
                "Net Filtration Pressure": {
                    "Normal Value": "Approximately 10 mmHg",
                    "Effect on Filtration": "Drives fluid across filtration barrier",
                    "Primary Determinant": "Combined hydrostatic and oncotic forces"
                },
                "Filtration Coefficient (Kf)": {
                    "Normal Value": "Product of permeability and surface area",
                    "Effect on Filtration": "Translates NFP into actual filtration rate",
                    "Primary Determinant": "Hydraulic permeability and capillary surface area"
                }
            }
        },
        {
            "slug": "barrier_injury_patterns",
            "title": "Filtration Barrier Injury Patterns",
            "subtitle": "Match each barrier component to mechanism, urinalysis, and example",
            "categories": ["Key Mechanism", "Urinalysis Pattern", "Example Condition"],
            "data": {
                "Podocytes": {
                    "Key Mechanism": "Foot process effacement reduces size selectivity",
                    "Urinalysis Pattern": "Selective proteinuria with minimal hematuria",
                    "Example Condition": "Minimal change disease, FSGS, membranous nephropathy"
                },
                "Glomerular Basement Membrane": {
                    "Key Mechanism": "Thinning, splitting reduces size and charge selectivity",
                    "Urinalysis Pattern": "Non-selective proteinuria with hematuria",
                    "Example Condition": "Alport syndrome, thin basement membrane disease"
                },
                "Endothelium": {
                    "Key Mechanism": "Loss of fenestrations with inflammatory injury",
                    "Urinalysis Pattern": "Mild-moderate proteinuria with hematuria, RBC casts",
                    "Example Condition": "IgA nephropathy, postinfectious GN, vasculitis"
                },
                "Mesangial Expansion": {
                    "Key Mechanism": "Increased matrix reduces capillary surface area",
                    "Urinalysis Pattern": "Mild-moderate proteinuria, variable hematuria and casts",
                    "Example Condition": "Diabetic kidney disease, IgA nephropathy"
                },
                "Mixed Combined Injury": {
                    "Key Mechanism": "Concurrent loss of selectivity and surface area",
                    "Urinalysis Pattern": "Heavy proteinuria with hematuria and cellular casts",
                    "Example Condition": "Lupus nephritis, MPGN, severe postinfectious GN"
                }
            }
        }
    ]
}
