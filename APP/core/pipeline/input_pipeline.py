class InputPipeline:
    def __init__(self, registry, system_schema):
        self.registry = registry
        self.system_schema = system_schema

    def dsp_pipeline(self, info, schema):
        result = {"correct_data": {}, "errors": {}}

        for field, value in info.items():

            if field in schema:
                rules = schema[field]

                if rules.get("required") and not value:
                    result["errors"][field] = "This field is required."
                    continue

                if not rules.get("required") and not value:
                    result["correct_data"][field] = None
                    continue

                cleaned = self.clean_input(value)
                normalized = self.dsp_normalize(field, cleaned)

                if not self.dsp_valid(field, normalized):
                    result["errors"][field] = f"Invalid value for {field}."
                else:
                    result["correct_data"][field] = normalized

            elif field in self.system_schema:
                result["correct_data"][field] = value

            else:
                result["errors"][field] = "This field is not in your schema."

        return result

    def clean_input(self, value):
        return value.strip() if isinstance(value, str) else value

    def dsp_valid(self, field, value):
        validators = self.registry.validators_handler()
        return validators.get(field, lambda _: False)(value)

    def dsp_normalize(self, field, value):
        normalizers = self.registry.normalizers_handler()
        return normalizers.get(field, lambda x: x)(value)



