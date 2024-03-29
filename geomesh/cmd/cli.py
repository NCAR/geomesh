import warnings

from geomesh.cmd.remesh_by_shape_factor import RemeshByShape
from geomesh.cmd.remesh import RemeshByDEM
from geomesh.cmd.mesh_upgrader import MeshUpgrader

class CmdCli:

    def __init__(self, parser):

        # TODO: Later add non experimental CLI through this class
        self._script_dict = {}

        scripts_subp = parser.add_subparsers(dest='scripts_cmd')
        for cls in [RemeshByShape, RemeshByDEM, MeshUpgrader]:
            item = cls(scripts_subp)
            self._script_dict[item.script_name] = item

    def execute(args):

        warnings.warn(
            "Scripts CLI is used for experimental new features"
            " and is subject to change.")

        args.scripts_cmd
        self._script_dict[args.scripts_cmd].run(args)
