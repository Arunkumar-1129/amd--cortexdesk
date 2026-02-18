function ResearchWorkspace() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Research Workspace</h1>
      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-xl font-semibold mb-4">Document Search</h2>
        <p className="text-gray-600 mb-4">
          Search your local documents using semantic search powered by RAG.
        </p>
        <div className="mb-4">
          <input
            type="text"
            placeholder="Ask a question about your documents..."
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <button className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">
          Search
        </button>
      </div>
    </div>
  );
}

export default ResearchWorkspace;

