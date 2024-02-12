from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.fhirdate import FHIRDate

# Your data (this should be replaced with your actual data)
data = {
  "name": "John Doe",
  "birth_date": "1980-01-01",
}

# Create a FHIR Patient resource
patient = Patient()

# Set the name
name = HumanName()
name.family = data["name"].split(" ")[1]
name.given = [data["name"].split(" ")[0]]
patient.name = [name]

# Set the birth date
patient.birthDate = FHIRDate(data["birth_date"])

# Now `patient` is a FHIR Patient resource
print(patient.json(indent=2))