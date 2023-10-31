from ..models import redaction

# Object redaction to dictionnary
def redaction_to_dict(a_redaction):
    return dict(a_redaction._mapping)

# Create a redaction with Json data
def create_redaction(json_data):
    return {
        'RefLivre': json_data.get('RefLivre'),
        'MatEtud': json_data.get('MatEtud')
    }