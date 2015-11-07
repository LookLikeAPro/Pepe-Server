from django.db.models.fields.related import ManyToManyRel, ManyToManyField, ManyToOneRel
from app.helpers.text import to_camel_case

def _to_dict(self, *args, **kwargs):
	if ('exclude' in kwargs):
		exclude_fields = kwargs['exclude']
	else:
		exclude_fields = ()
	if ('include' in kwargs):
		include_fields = kwargs['include']
	else:
		include_fields = ()
	if ('camel_case' in kwargs):
		camel_case = True if kwargs['camel_case'] else False
	else:
		camel_case = True
	data = {}
	for field in self._meta.get_fields():
		if camel_case:
			field_name = to_camel_case(field.name)
		else:
			field_name = field.name
		if field.name in exclude_fields:
			continue
		if isinstance(field, ManyToOneRel):
			pass
		elif isinstance(field, ManyToManyField):
			pass
		elif isinstance(field, ManyToManyRel):
			pass
		else:
			data[field_name] = field.value_from_object(self)
	return data
