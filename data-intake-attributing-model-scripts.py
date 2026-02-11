# ============================================================
# LRSP Model – Field Calculation Helper Functions
# Extracted from ArcGIS Pro ModelBuilder CalculateField tools
# ============================================================


## ------------------------------------------------------------
## Function: get_severity_code
## Description: Converts ExtentOfInjuryCode → numeric severity
## ------------------------------------------------------------
def get_severity_code(severity):
    if severity is None:
        return 0

    severity_dict = {
        "PossibleInjury": 1,
        "OtherVisibleInactive": 2,
        "ComplaintOfPainInactive": 3,
        "SuspectMinor": 4,
        "SuspectSerious": 5,
        "SevereInactive": 6,
        "Fatal": 7
    }

    return severity_dict.get(severity, 0)



## ------------------------------------------------------------
## Function: classify_severity
## Description: Converts numeric severity → generalized category
## ------------------------------------------------------------
def classify_severity(value):
    try:
        v = int(value)
    except:
        return "No Injury"

    if v in [1, 2, 3]:
        return "Complaint of Pain"
    elif v == 4:
        return "Injury (Minor)"
    elif v in [5, 6]:
        return "Injury (Serious)"
    elif v == 7:
        return "Fatal"
    else:
        return "No Injury"



## ------------------------------------------------------------
## Function: assign_drug_or_alcohol
## Description: Flags drug/alcohol involvement based on description
## ------------------------------------------------------------
def assign_drug_or_alcohol(value):
    if value is None:
        return "No"

    yes_values = [
        "HBD-UNDER INFLUENCE",
        "IMPAIRMENT-PHYSICAL",
        "UNDER_DRUG_INFLUENCE"
    ]

    no_values = [
        "HAD NOT BEEN DRINKING",
        "HBD-IMPAIRMENT UNKNOWN",
        "HBD-NOT UNDER INFLUENCE",
        "IMPAIRMENT_NOT_KNOWN",
        "NOT APPLICABLE",
        "SLEEPY/FATIGUED"
    ]

    if value in yes_values:
        return "Yes"
    elif value in no_values:
        return "No"
    else:
        return "No"



## ------------------------------------------------------------
## Function: categorize_time_of_day
## Description: Converts HHMM time → generalized time-of-day category
## ------------------------------------------------------------
def categorize_time_of_day(time):
    if time is None:
        return None

    try:
        t = int(time)
    except:
        return None

    if 900 <= t <= 1500:
        return "Midday / Off-Peak (9AM to 3PM)"
    elif 1501 <= t <= 1900:
        return "Evening Peak (3PM to 7PM)"
    elif 1901 <= t <= 2200:
        return "Nighttime (7PM to 10PM)"
    elif 2201 <= t <= 2400 or 0 <= t <= 600:
        return "Overnight (10PM to 6AM)"
    elif 601 <= t <= 859:
        return "Morning Peak (6AM to 10AM)"
    else:
        return "Uncategorized"



## ------------------------------------------------------------
## Function: assign_mode
## Description: Converts vehicle type → generalized mode category
## ------------------------------------------------------------
def assign_mode(desc):
    if desc is None:
        return "Other"

    bicycle = ["Bicycle", "MotorizedBicycle", "ElectricBicycles"]
    motorcycle = ["Motorcycle"]
    truck = [
        "Firetruck", "PickupsAndPanels", "PickupWithCamper", "TruckTractor",
        "TwoAxleTruck", "TwoAxleTowTruck", "ThreeOrMoreAxleTruck",
        "SemiTankTrailer", "TwoTrailersIncludesSemiAndPull",
        "TwoAxleTankTruck", "SemiTrailer", "HmTruckTractor",
        "ThreeAxleTankTruck", "TrailerCoach", "HmwTruckTractor"
    ]
    vehicle = [
        "MiniVan", "PassengerCarStationWagonJeep",
        "OtherUnknownHitAndRunDriver", "PoliceCar",
        "SportUtilityVehicle", "AllTerrainVehicle", "DuneBuggy",
        "SchoolBusPublicTypeI", "Paratransit",
        "MotorHome40FeetOrLonger", "MiscMotorVehicleSnowmobileGolfCart"
    ]
    pedestrian = ["Pedestrian"]
    other = ["MiscNonMotorVehicle", "HighwayConstructionEquipment"]

    if desc in bicycle:
        return "Bicycle"
    elif desc in motorcycle:
        return "Motorcycle"
    elif desc in truck:
        return "Truck"
    elif desc in vehicle:
        return "Vehicle"
    elif desc in pedestrian:
        return "Pedestrian"
    elif desc in other:
        return "Other"
    else:
        return "Other"
