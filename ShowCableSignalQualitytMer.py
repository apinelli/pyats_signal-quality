'''
Author: Angelo Pinelli
March 30th, 2022
'''
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# ======================================================
# Schema for 'show cable signal-quality mer'
# ======================================================


class ShowCableSignalQualitytMerSchema(MetaParser):
    schema = {
        'I/F': {
            Any(): {
                'mer': str,
                'samples': str
            }
        }
    }


class ShowCableSignalQualitytMer(ShowCableSignalQualitytMerSchema):
    """Parser for show show cable signal-quality mer on Cisco CBR8 devices
    parser class - implements detail parsing mechanisms for cli output.
    """
    cli_command = 'show cable signal-quality mer'

    """
    Load for five secs: 7%/1%; one minute: 9%; five minutes: 9%
    Time source is NTP, 15:17:00.744 EDT Sat Mar 26 2022
    I/F               Received MER    Received MER
                    (dB)            Samples
    Cable1/0/0/U0     39.13           1            
    Cable1/0/0/U1     39.13           1            
    Cable1/0/0/U2     38.16           1            
    Cable1/0/0/U3     36.70           1            
    Cable1/0/0/U4     -----           -----        
    Cable1/0/0/U5     -----           -----        
    Cable1/0/0/U6     -----           -----        
    <snip>
    Cable9/0/15/U15   -----           -----           7 
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        cable_sig_quality_mer_dict = {}

        result_dict = {}

        p0 = re.compile(r'^(?P<interface>Cable\d\/0/\d+/U\d+)\s+(?P<mer>\d+.\d+)\s+(?P<samples>\d+)')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'I/F' not in cable_sig_quality_mer_dict:
                    result_dict = cable_sig_quality_mer_dict.setdefault('I/F',{})
                interface = m.groupdict()['interface']
                mer = m.groupdict()['mer']
                samples = m.groupdict()['samples']
                result_dict[interface] = {}
                result_dict[interface]['mer'] = mer
                result_dict[interface]['samples'] = samples
                continue
        return cable_sig_quality_mer_dict
