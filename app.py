from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.fhirdate import FHIRDate
from fhir.resources.medication import Medication
from fhir.resources.detectedissue import DetectedIssue
from fhir.resources.allergyintolerance import AllergyIntolerance
from fhir.resources.condition import Condition
from fhir.resources.familymemberhistory import FamilyMemberHistory

# Create a FHIR Patient resource
patient = Patient()
name = HumanName()
name.family = "Doe"
name.given = ["John"]
patient.name = [name]
patient.birthDate = FHIRDate("1980-01-01")

# Create a FHIR Medication resource
medication = Medication()
medication.status = "active"
medication.code = {"text": "Aspirin"}

# Create a FHIR DetectedIssue resource
detected_issue = DetectedIssue()
detected_issue.status = "final"

# Create a FHIR AllergyIntolerance resource
allergy_intolerance = AllergyIntolerance()
allergy_intolerance.clinicalStatus = {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical", "code": "active"}]}

# Create a FHIR Condition resource
condition = Condition()
condition.clinicalStatus = {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/condition-clinical", "code": "active"}]}

# Create a FHIR FamilyMemberHistory resource
family_member_history = FamilyMemberHistory()
family_member_history.status = "completed"

# Now you have FHIR resources for each of the requested types