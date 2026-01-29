class InputPipeline:
    def __init__(self, sys_ctrl):
        self.sys_ctrl = sys_ctrl
            
    def dsp_pipeline(self, info, schema, system_schema):
        """
        Pipeline to validate, normalize, and clean user input.
        Handles user schema, system schema, and unknown fields.
        Does NOT add defaults for system fields.
        
        Returns:
            wrongs: dict of errors
            correct_data: dict of cleaned/normalized input
        """
        normalize_results = {"correct_data": {}, "errors": {}}

        for field, value in info.items():

            if field in schema:
                # User field
                field_schema = schema[field]

                if field_schema.get("required") and not value:
                    normalize_results["errors"][field] = "This field is required."
                    continue

                elif not field_schema.get("required") and not value:
                    normalize_results["correct_data"][field] = None
                    continue

                # Clean, normalize, validate
                cleaned_value = self.clean_input(value)
                normalized_value = self.dsp_normalize(field, cleaned_value)
                is_valid = self.dsp_valid(field, normalized_value)

                if not is_valid:
                    normalize_results["errors"][field] = f"Invalid value for {field}."
                else:
                    normalize_results["correct_data"][field] = normalized_value

            elif field in system_schema:
                # System field, accept as-is
                normalize_results["correct_data"][field] = value

            else:
                # Unknown field
                normalize_results["errors"][field] = "This field is not in your schema."

        return normalize_results
    
    
    def clean_input(input):
        if isinstance(input, str):
            return input.strip()
        return input

    def dsp_valid(self, field, value):
        validators_map = self.sys_ctrl.Registry.validators_handler()

        if field not in validators_map:
            return False

        return validators_map[field](value)

    def dsp_normalize(self, field, value):
        normalizers_map = self.sys_ctrl.Registry.normalizers_handler()

        if field not in normalizers_map:
            return value

        return normalizers_map[field](value)
