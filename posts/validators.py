from django.core.exceptions import ValidationError

def validate_symbols(value):
    if ("@" in value) or ("#" in value):
        raise ValidationError('"@"와 "#"는 포함될수 없습니다.', code='symbor-err')