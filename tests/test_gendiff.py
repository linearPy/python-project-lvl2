from gendiff.gendiff import generate_diff


FLAT_JSON_1 = 'tests/fixtures/flat_1.json'
FLAT_JSON_2 = 'tests/fixtures/flat_2.json'
FLAT_YAML_1 = 'tests/fixtures/flat_1.yml'
FLAT_YAML_2 = 'tests/fixtures/flat_2.yml'
FLAT_ANSWER = 'tests/fixtures/flat_answer'


def get_expected_text(path):
    with open(path) as answer:
        answer = answer.read()

    return answer


def test_generate_diff():
    assert generate_diff(FLAT_JSON_1, FLAT_JSON_2) == \
           get_expected_text(FLAT_ANSWER)

    assert generate_diff(FLAT_YAML_1, FLAT_YAML_2) == \
           get_expected_text(FLAT_ANSWER)
