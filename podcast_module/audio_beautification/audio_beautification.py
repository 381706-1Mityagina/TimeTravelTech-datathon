# Load your main audio file
main_audio = "C:/Users/darya/Documents/Study/Datathon/gpt_module/Renaissance_Leonardo-da-Vinci_rus_onyx.mp3"
# Load your background music
background_music = "C:/Users/darya/Documents/Study/Datathon/gpt_module/silent-wood.mp3"

import soundfile as sf
import numpy as np

def mix_audio(main_audio_path, background_music_path, output_path, background_volume_reduction):
    main_audio, main_fs = sf.read(main_audio_path)
    background_music, bg_fs = sf.read(background_music_path)
    
    delay_seconds = 5
    delay_samples = int(main_fs * delay_seconds)
    main_audio_with_delay = np.concatenate([np.zeros(delay_samples), main_audio])

    # Audio length alignment
    min_length = min(len(main_audio_with_delay), len(background_music))
    main_audio_with_delay = main_audio_with_delay[:min_length]
    background_music = background_music[:min_length]

    # Reducing the dimension of background music if it is stereo
    if len(background_music.shape) == 2:
        background_music = np.mean(background_music, axis=1)

    # Reducing background music volume
    background_music /= 5 ** (background_volume_reduction / 20.0)

    # Mix audio
    mixed_audio = main_audio_with_delay + background_music

    # Normalization to avoid distortion
    mixed_audio /= np.max(np.abs(mixed_audio))
    
    # Additional seconds of background music after main audio ends
    background_duration_after_main = 5
    additional_samples = int(main_fs * background_duration_after_main)
    mixed_audio = np.concatenate([mixed_audio, background_music[-additional_samples:]])

    # Save mixed audio
    sf.write(output_path, mixed_audio, main_fs)
