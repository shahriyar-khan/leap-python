import typer

import ssg.parsers
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {"source": source,
              "dest": dest,
              "parsers": [ssg.parsers.ResourceParser()]}

    site_instance = Site(**config).build()


typer.run(main)