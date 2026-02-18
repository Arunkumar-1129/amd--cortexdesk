function Dashboard() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-2">Tasks</h2>
          <p className="text-gray-600">Manage your tasks and action items</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-2">Meetings</h2>
          <p className="text-gray-600">Live meeting mode and summaries</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-2">Research</h2>
          <p className="text-gray-600">Search your local documents</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;

