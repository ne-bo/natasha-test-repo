import pytest
from elasticsearch_stress_test import stress_test

class Test:

    @pytest.mark.parametrize("NUMBER_OF_INDICES", [1, 10, 100])
    @pytest.mark.parametrize("NUMBER_OF_DOCUMENTS", [1])
    @pytest.mark.parametrize("NUMBER_OF_CLIENTS", [1])
    @pytest.mark.parametrize("NUMBER_OF_SECONDS", [120])
    @pytest.mark.parametrize("NUMBER_OF_SHARDS", [1, 10, 100])
    @pytest.mark.parametrize("NUMBER_OF_REPLICAS", [1])
    @pytest.mark.parametrize("BULK_SIZE", [1, 10, 100])
    @pytest.mark.parametrize("MAX_FIELDS_PER_DOCUMENT", [100])
    @pytest.mark.parametrize("MAX_SIZE_PER_FIELD", [1000])
    @pytest.mark.parametrize("NO_CLEANUP", [False])
    @pytest.mark.parametrize("STATS_FREQUENCY", [30])
    @pytest.mark.parametrize("WAIT_FOR_GREEN", [False])

    def test_eval(self, NUMBER_OF_INDICES, NUMBER_OF_DOCUMENTS, NUMBER_OF_CLIENTS, NUMBER_OF_SECONDS, NUMBER_OF_SHARDS,
                NUMBER_OF_REPLICAS, BULK_SIZE, MAX_FIELDS_PER_DOCUMENT, MAX_SIZE_PER_FIELD,
                NO_CLEANUP,STATS_FREQUENCY, WAIT_FOR_GREEN):
        print("natasha")
        stress_test(NUMBER_OF_INDICES, NUMBER_OF_DOCUMENTS, NUMBER_OF_CLIENTS, NUMBER_OF_SECONDS, NUMBER_OF_SHARDS,
                NUMBER_OF_REPLICAS, BULK_SIZE, MAX_FIELDS_PER_DOCUMENT, MAX_SIZE_PER_FIELD,
                NO_CLEANUP,STATS_FREQUENCY, WAIT_FOR_GREEN,
                'search-natasha-domain-1-bx2wv5limgi43nvb7cti3o2dcu.us-west-2.es.amazonaws.com')

