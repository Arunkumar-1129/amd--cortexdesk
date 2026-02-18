function Meetings() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Meetings</h1>
      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-xl font-semibold mb-4">Live Meeting Mode</h2>
        <p className="text-gray-600 mb-4">
          Toggle live meeting mode to capture and process audio in real-time.
        </p>
        <button className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
          Start Meeting Mode
        </button>
      </div>
    </div>
  );
}

export default Meetings;

