from scripts.reverb_parameters_optimize import *

plt.switch_backend('agg')

if __name__ == "__main__":

    rir_name = 'spergair'
    folder = f'stereo/{rir_name}/'

    rir_path = f'audio/input/chosen_rirs/{folder}/_todo/'
    er_path = f'audio/trimmed_rirs/{folder}'
    armodel_path = f'audio/armodels/{folder}'
    merged_rir_path = f'audio/merged_rirs/{folder}'
    vst_rir_path = f'audio/vst_rirs/{folder}'
    params_path = f'audio/params/{folder}'
    result_path = f'audio/results/{folder}'
    input_path = f'audio/input/sounds/48/speech/_trimmed/loudnorm/_todo/'

    find_params(rir_path,
                er_path,
                armodel_path,
                merged_rir_path,
                vst_rir_path,
                params_path,
                result_path,
                input_path,
                generate_references=False,
                original_er=False,
                pre_norm=False)




