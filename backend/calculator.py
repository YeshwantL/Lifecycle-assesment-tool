import pandas as pd
from model import predict_energy_if_missing 

try:
    lci_data = pd.read_csv('data/lci_data.csv')
except FileNotFoundError:
    print("Error: lci_data.csv not found. Make sure it's in the /data folder.")
    lci_data = None

def perform_calculations(tons, recycled_percent):
    if lci_data is None:
        return {"error": "LCI (Life Cycle Inventory) data not loaded."}

    recycled_ratio = recycled_percent / 100.0
    primary_ratio = 1 - recycled_ratio

    primary_tons = tons * primary_ratio
    secondary_tons = tons * recycled_ratio

    primary_impacts = lci_data[lci_data['Process'] == 'Primary'].set_index('ImpactCategory')['Value']
    secondary_impacts = lci_data[lci_data['Process'] == 'Secondary'].set_index('ImpactCategory')['Value']

    circular_carbon = (primary_tons * primary_impacts['Carbon Emissions']) + (secondary_tons * secondary_impacts['Carbon Emissions'])
    circular_energy = (primary_tons * primary_impacts['Energy Consumption']) + (secondary_tons * secondary_impacts['Energy Consumption'])
    circular_water = (primary_tons * primary_impacts['Water Usage']) + (secondary_tons * secondary_impacts['Water Usage'])
    
    predict_energy_if_missing(recycled_percent)

    linear_carbon = tons * primary_impacts['Carbon Emissions']
    linear_energy = tons * primary_impacts['Energy Consumption']
    linear_water = tons * primary_impacts['Water Usage']

    carbon_saved = linear_carbon - circular_carbon
    energy_saved = linear_energy - circular_energy
    water_saved = linear_water - circular_water

    results = {
        "circularScenario": {
            "carbonEmissions": round(circular_carbon, 2),
            "energyConsumption": round(circular_energy, 2),
            "waterUsage": round(circular_water, 2)
        },
        "linearScenario": {
            "carbonEmissions": round(linear_carbon, 2),
            "energyConsumption": round(linear_energy, 2),
            "waterUsage": round(linear_water, 2)
        },
        "savings": {
            "carbonSaved": round(carbon_saved, 2),
            "energySaved": round(energy_saved, 2),
            "waterSaved": round(water_saved, 2)
        }
    }

    return results