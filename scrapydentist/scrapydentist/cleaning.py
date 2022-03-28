from __future__ import nested_scopes
from .helpers.cleanPhoneNumbers import extract_phones

class CleaningPipeline:
    def group_values(self, item, type):
        value_list = item.pop(f'{type}s', [])
        single_value = item.pop(type, None)
        if single_value:
            value_list.append(single_value)
        return value_list
    def process_item(self, item, spider):
        phone=extract_phones(self.group_values(item,'phone'))
        print(phone)
        return dict(
            **item,
            # text=dict(text),
            phones=phone,
            # emails=emails,
            # links=links,
            # images=images,
        )

