import argparse
from enum import Enum

import semver


class UpdatedState(Enum):
    no_changes = 'no_changes'
    incompatible = 'incompatible'
    compatible = 'compatible'


def main(args: argparse.Namespace) -> None:
    assert args.updated_state is not UpdatedState.no_changes

    ver = semver.VersionInfo.parse(args.curr_version.strip())

    process_ver = {
        UpdatedState.compatible: lambda v: v.bump_minor(),
        UpdatedState.incompatible: lambda v: v.bump_major()
    }
    ver = process_ver[args.updated_state](ver)

    print(ver)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--curr-version", type=str, help="Current package version", required=True)
    parser.add_argument("--updated-state", type=UpdatedState, help="Current package version", required=True)
    args = parser.parse_args()

    main(args)
