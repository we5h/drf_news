from drf_yasg.generators import OpenAPISchemaGenerator


def my_custom_openapi_schema_generator(path_prefix:str):
    if not isinstance(path_prefix, str):
        raise TypeError('The supplied path_prefix must be of type str')

    class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
        def get_schema(self, *args, **kwargs):
            schema = super().get_schema(*args, **kwargs)
            schema.basePath = path_prefix
            return schema
    return CustomOpenAPISchemaGenerator