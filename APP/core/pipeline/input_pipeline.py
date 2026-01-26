def input_pipeline_dispatcher(sys_ctrl, info, schema, system_schema):
    """
    Pipeline to validate, normalize, and clean user input.
    Handles user schema, system schema, and unknown fields.
    Does NOT add defaults for system fields.
    
    Returns:
        wrongs: dict of errors
        correct_data: dict of cleaned/normalized input
    """
    dsp = sys_ctrl.dispatcher
    correct_data = {}
    wrongs = {}

    for field, value in info.items():

        if field in schema:
            # User field
            field_schema = schema[field]

            if field_schema.get("required") and not value:
                wrongs[field] = "This field is required."
                continue

            elif not field_schema.get("required") and not value:
                correct_data[field] = None
                continue

            # Clean, normalize, validate
            cleaned_value = sys_ctrl.helpers.clean_input(value)
            normalized_value = dsp.dispatch_normalizer(field, cleaned_value)
            is_valid = dsp.dispatch_validator(field, normalized_value)

            if not is_valid:
                wrongs[field] = f"Invalid value for {field}."
            else:
                correct_data[field] = normalized_value

        elif field in system_schema:
            # System field, accept as-is
            correct_data[field] = value

        else:
            # Unknown field
            wrongs[field] = "This field is not in your schema."

    return wrongs, correct_data
