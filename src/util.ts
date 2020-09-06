export const getAttribute = (attributeName: string) => {
	return ((process.argv || []).find((arg) => arg.startsWith('--port')) || '').split('=')[1];
}
