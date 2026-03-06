from databricks.sdk.runtime import spark
from pyspark.sql import DataFrame
from databricks.sdk import WorkspaceClient


def test_find_all_taxis():
    # Test reading secret value
    w = WorkspaceClient()
    secret_value = w.secrets.get_secret(scope="am_read_yahoo_scope", key="service_name")
    assert secret_value is not None, "Secret value should not be None"