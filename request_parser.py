#!/usr/bin/python3

import sys

class Request():
	def __init__(self, req_file):
		with open(req_file) as req:
			self._raw_req = req.read()
			self._req_lines = self._raw_req.split('\n')
		self._req_startline = self.req_lines[0]
		self._req_headerlines = self.req_lines[1:self.req_lines.index("")]
		self._req_data = self.raw_req[self.raw_req.find("\n\n") + 2:].rstrip()
		self._headers = {}
		for hl in self._req_headerlines:
			k, v = hl.split(": ")
			self._headers[k] = v
		self._req_method, self._req_path, self._req_version = self.startline.split()

	@property
	def raw_req(self):
		return self._raw_req

	@property
	def req_lines(self):
		return self._req_lines

	@property
	def startline(self):
		return self._req_startline

	@property
	def method(self):
		return self._req_method
	
	@property
	def path(self):
		return self._req_path

	@property
	def version(self):
		return self._req_version

	@property
	def header_lines(self):
		return self._req_headerlines

	@property
	def headers(self):
		return self._headers

	@property
	def body(self):
		return self._req_data


if __name__ == "__main__":
	req = Request("req.txt")
	print(req.startline)
	for h, v in req.headers.items():
		print(f"{h}: {v}")
	print(req.body)
