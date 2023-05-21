
export const getWebcams = async () => {
  const response = await fetch(`/api/webcams`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  });

  const webcamIds = (await response.json()) as number[];
  return webcamIds;
}