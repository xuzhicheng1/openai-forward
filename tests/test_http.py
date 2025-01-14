import os
import time
from sparrow.multiprocess import kill
import subprocess
import httpx
from utils import rm


class TestRun:
    @classmethod
    def setup_class(cls):
        kill(8000)
        base_url = "https://caloi.top/openai"
        subprocess.Popen(["nohup", "openai-forward", "run", "--base_url", base_url])
        time.sleep(3)

    @classmethod
    def teardown_class(cls):
        kill(8000)
        rm("nohup.out")

    def test_get_doc(self):
        resp = httpx.get("http://localhost:8000/docs")
        assert resp.is_success

    def test_get_chat_completions(self):
        resp = httpx.get("http://localhost:8000/v1/chat/completions")
        assert resp.status_code == 401
