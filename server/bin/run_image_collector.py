import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from ebretail.components.image_collector import ImageCollector

collector = ImageCollector()

collector.main()
