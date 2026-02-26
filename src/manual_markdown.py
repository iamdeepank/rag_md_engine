"""Specific Manual Markdown Implementation."""

from logging import getLogger
from pathlib import Path
from .datacontract import MarkdownDataContract, NoSettings, TypedStep

log = getLogger(__name__)


class DeMarkdownStep(TypedStep[NoSettings, None, list[MarkdownDataContract]]):
   """Return local Markdown files."""


   path = Path(__file__).parent / "data/"

   def get_paths(self) -> list[Path]:
       """Get md paths.


       Returns:
           list[Path]: mds


       """
       if not self.path.exists():
           log.warning("Directory not found: '%s' NO docs retrieved", self.path.as_posix())
           return []
       return [
           *self.path.rglob("*.md"),
           *self.path.rglob("*.Md"),
           *self.path.rglob("*.MD"),
           *self.path.rglob("*.mD"),
       ]


   def run(self, inpt: None) -> list[MarkdownDataContract]:
       return [MarkdownDataContract.from_file(fp) for fp in self.get_paths()]

