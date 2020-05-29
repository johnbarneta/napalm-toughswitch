"""napalm_mikrotik package."""

# Import stdlib
import pkg_resources

# Import local modules
from napalm_toughswitch.toughswitch import ToughSwitchDriver

try:
    __version__ = pkg_resources.get_distribution('napalm-toughswitch').version
except pkg_resources.DistributionNotFound:
    __version__ = "Not installed"

__all__ = ('ToughSwitchDriver', )
