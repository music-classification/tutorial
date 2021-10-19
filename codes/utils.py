import torch
import matplotlib.pyplot as plt


def plot_spectrogram(
    waveform: torch.Tensor,
    sample_rate: int,
    title: str = "Spectrogram",
    xlim: int = None,
):
    """From: https://pytorch.org/tutorials/beginner/audio_preprocessing_tutorial.html"""
    waveform = waveform.numpy()
    num_channels, _ = waveform.shape

    fig, axes = plt.subplots(num_channels, 1)
    if num_channels == 1:
        axes = [axes]
    for c in range(num_channels):
        axes[c].specgram(waveform[c], Fs=sample_rate, scale="dB")
        if num_channels > 1:
            axes[c].set_ylabel(f"Channel {c+1}")
        if xlim:
            axes[c].set_xlim(xlim)
    fig.suptitle(title)
    plt.show(block=False)
