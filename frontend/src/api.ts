export interface ApiResponse {
  user_id: number;
  user_name: string;
}

export const fetchUsers = async (): Promise<ApiResponse[]> => {
  const response = await fetch(`http://localhost:8000/users`);
  if (!response.ok) {
    throw new Error("Network response was not ok");
  }
  return response.json();
};
