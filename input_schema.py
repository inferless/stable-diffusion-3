INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["a living room, bright modern Scandinavian style house, large windows, magazine photoshoot, 8k, studio lighting"]
    },
    "negative_prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["low quality"]
    }
}