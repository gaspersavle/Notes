# 1. Analiza skripte

```python
class DetectionLoader():
	def __init__(self, detector, cfg, opt)
		self.cfg = cfg 
		"""Uvozi konfiguracijo iz alphapose.utils.configs"""
		self.opt = opt # ne stekam]
		self.device = opt.device
		"""Nastavi napravo na kateri deluje,
		pri nas bo vedno cuda"""
		self.detector = detector
		"""Detektor nastavi na 'tracker'"""

		self._input_size = cfg.DATA_PRESET.IMAGE_SIZE
		self._output_size = cfg.DATA_PRESET.HEATMAP_SIZE

		self._sigma = cfg.DATA_PRESET.SIGMA

		pose_dataset = builder.retrieve_dataset(self.cfg.DATASET.TRAIN)
```