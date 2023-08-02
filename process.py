import subprocess

from job import JobData


class Processor:
    def __init__(self, logger):
        self.logs = logger

    def process_image(self, job_base):
        job_data = JobData(job_base)
        job_type = job_data.data.get("JOB")
        self._get_processor(job_type, job_data)

    def _get_processor(self, job_type, job_data):
        if job_type == "radius_tibia_final":
            self._radius_tibia_final(job_data)

    def _radius_tibia_final(self, job_data):
        proc = subprocess.Popen("cd {} && python3 segment.py --image-pattern {} --masks-subdirectory {}".format(BATCHES, self.get_image_name(), MASKS))
        proc.wait()
        x = subprocess.Popen()
        x.wait()