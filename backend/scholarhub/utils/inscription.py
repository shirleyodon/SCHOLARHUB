from ..models import inscription

# Object inscription to dictionnary
def inscription_to_dict(an_inscription):
    return dict(an_inscription._mapping)

# Create an inscription with Json data
def create_inscription(json_data):
    return {
        'MatEtud': json_data.get('MatEtud'),
        'IdNiv': json_data.get('IdNiv'),
        'CodeAnnee': json_data.get('CodeAnnee')
    }