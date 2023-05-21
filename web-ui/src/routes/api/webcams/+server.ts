import { PUBLIC_WEBCAM_SERVER } from '$env/static/public';
import { json } from '@sveltejs/kit';

/** @type {import('./$types').RequestHandler} */
export async function GET({ }) {
  const url = `${PUBLIC_WEBCAM_SERVER}/webcams`
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  });

  const webcamIds = (await response.json()) as number[];
  return json(webcamIds);
}